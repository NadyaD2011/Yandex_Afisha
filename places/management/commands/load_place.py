from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from decimal import Decimal

import requests

from places.models import Place, Image


def get_json_info_by_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def parse_place_with_images(url):
    try:
        place = get_json_info_by_url(url)
        parsed_place = Place.objects.get_or_create(
            title=place['title'],
            defaults={
                'short_description': place['short_description'],
                'long_description': place['long_description'],
                'lat': Decimal(place['coordinates']['lat']),
                'lng': Decimal(place['coordinates']['lng']),
            }
        )[0]
        for img_number, img_url in enumerate(place['imgs']):
            response = requests.get(img_url)
            response.raise_for_status()
            img_content = ContentFile(response.content)
            img_name = '{} {}.jpg'.format(img_number + 1, parsed_place.title)
            existing_image = Image.objects.filter(img_url=img_url).first()
            if existing_image:
                continue
            image_instance = Image(
                place=parsed_place,
                img_url=img_url
            )
            image_instance.img.save(img_name, img_content, save=True)
    except requests.exceptions.HTTPError or\
            requests.exceptions.ConnectionError:
        pass


class Command(BaseCommand):
    help = 'Download json data with url or with local path and parse it to DB.'

    def handle(self, *args, **options):
        parse_place_with_images(options['url'])

    def add_arguments(self, parser):
        parser.add_argument(
            'url', help='Path to json-file in the Inthernet'
        )

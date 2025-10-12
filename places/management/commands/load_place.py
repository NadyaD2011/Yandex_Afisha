from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from decimal import Decimal

import requests

from places.models import Place, Image


def save_img(img_url, img_number, parsed_place):
    try:
        if Image.objects.filter(place=parsed_place, index=img_number).exists():
            return

        response = requests.get(img_url)
        response.raise_for_status()
        img_content = ContentFile(response.content, f"{img_number + 1} {parsed_place.title}.jpg")

        Image.objects.create(
            place=parsed_place,
            original_url=img_url,
            index=img_number,
            img=img_content
        )
    except requests.exceptions.HTTPError or\
            requests.exceptions.ConnectionError:
        print('Произошла ошибка')


def parse_place_with_images(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        place = response.json()
        parsed_place = Place.objects.get_or_create(
            title=place['title'],
            defaults={
                'short_description': place['description_short'],
                'long_description': place['description_long'],
                'lat': Decimal(place['coordinates']['lat']),
                'lng': Decimal(place['coordinates']['lng']),
            }
        )[0]
        for img_number, img_url in enumerate(place['imgs'], start=1):
            save_img(img_url, img_number, parsed_place)
    except requests.exceptions.HTTPError or\
            requests.exceptions.ConnectionError:
        print('Произошла ошибка')


class Command(BaseCommand):
    help = 'Download json data with url or with local path and parse it to DB.'

    def handle(self, *args, **options):
        parse_place_with_images(options['url'])

    def add_arguments(self, parser):
        parser.add_argument(
            'url', help='Path to json-file in the Inthernet'
        )

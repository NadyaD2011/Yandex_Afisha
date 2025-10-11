from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template import loader
from django.urls import reverse

from places.models import Place, Image


def parse_place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('imgs'), id=place_id)
    images_urls = [image.img.url for image in place.imgs.all()]

    payload = {
        'title': place.title,
        'imgs': images_urls,
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lng': float(place.lng),
            'lat': float(place.lat),
        }
    }

    return JsonResponse(payload, json_dumps_params={'ensure_ascii': False})


def open_map(request):
    places = Place.objects.all()

    features = [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            'short_description': place.short_description or '',
            'long_description': place.long_description or '',
            "coordinates": {
                "lat": place.lat,
                "lng": place.lng
            },
            'detailsUrl': reverse('parse_place_details', kwargs={'place_id': place.id})
          }
        }
        for place in places
    ]
    context = {
        'places': {
            'type': "FeatureCollection",
            'features': features,
        }
    }

    return render(request, 'index.html', context)

from django.http import JsonResponse
from django.template import loader
from places.models import Place, Image

from django.shortcuts import render, get_object_or_404
from django.urls import reverse


def parse_place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=place_id)
    images_urls = [image.image.url for image in place.images.all()]

    payload = {
        'title': place.title,
        'imgs': images_urls,
        'short_description': place.description_short,
        'long_description': place.description_long,
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
            "coordinates": [place.lat, place.lng]
          },
          "properties": {
            "title": place.title,
            "placeId": "moscow_legends",
            'description_short': place.description_short,
            'description_long': place.description_long,
            "coordinates": {
                "lng": place.lng,
                "lat": place.lat
            },
            'detailsUrl': reverse('parse_place_details', kwargs={'place_id': place.id})
            # "detailsUrl": "{% static '/places/moscow_legends.json' %}"
          }
        }
        for place in places
    ]
    context = {
        'places': {
            'type': "FeatureCollection",
            'features': features
        }
    }

    return render(request, 'index.html', context)

from django.http import HttpResponse
from django.template import loader
from places.models import Place

from django.shortcuts import render


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
            "detailsUrl": "{% static '/places/moscow_legends.json' %}"
          }
        }
        for place in places
    ]
    context = {'places': {
            'type': "FeatureCollection",
            'features': features
        }
    }

    return render(request, 'index.html', context)

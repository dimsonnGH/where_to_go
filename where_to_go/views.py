from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from where_to_go.settings import STATIC_URL
from places.models import Place


def index(request) :
    places = Place.objects.all()
    features = [{
        "type" : "Feature",
        "geometry" : {
            "type" : "Point",
            "coordinates" : [place.longitude, place.latitude]
        },
        "properties" : {
            "title" : place.title,
            "placeId" : place.placeId,
            "detailsUrl" : "url"
        }
    } for place in places]

    places_geojson = {
        "type" : "FeatureCollection",
        "features" : features}

    data = {"places_geojson" : places_geojson}

    return render(request, 'index.html', data)

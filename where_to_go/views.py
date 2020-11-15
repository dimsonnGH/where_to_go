from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from where_to_go.settings import STATIC_URL
from places.models import Place, PlaceImage


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


def place_json(request, placeId) :
    place = get_object_or_404(Place, placeId=placeId)
    images = PlaceImage.objects.filter(place=place)
    data = {
        "title" : place.title,
        "imgs" : [image.image.url for image in images],
        "description_short" : place.description_short,
        "description_long" : place.description_long,
        "coordinates" : {
            "lng" : place.longitude,
            "lat" : place.latitude
        }
    }

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})

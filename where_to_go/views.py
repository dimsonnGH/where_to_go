from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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
            "placeId" : place.place_id,
            "detailsUrl" : reverse('place_json', kwargs={'place_id':place.place_id})
        }
    } for place in places]

    places_geojson = {
        "type" : "FeatureCollection",
        "features" : features}

    context = {"places_geojson" : places_geojson}

    return render(request, 'index.html', context)


def place_json(request, place_id) :
    place = get_object_or_404(Place.objects.prefetch_related('images'), place_id=place_id)
    response_data = {
        "title" : place.title,
        "imgs" : [image.image.url for image in place.images.all()],
        "description_short" : place.description_short,
        "description_long" : place.description_long,
        "coordinates" : {
            "lng" : place.longitude,
            "lat" : place.latitude
        }
    }

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from where_to_go.settings import STATIC_URL


def index(request) :
    places_geojson = {
        "type" : "FeatureCollection",
        "features" : [
            {
                "type" : "Feature",
                "geometry" : {
                    "type" : "Point",
                    "coordinates" : [37.62, 55.793676]
                },
                "properties" : {
                    "title" : "Легенды Москвы",
                    "placeId" : "moscow_legends",
                    "detailsUrl" : ".{0}{1}".format(STATIC_URL, 'places/moscow_legends.json')
                }
            },
            {
                "type" : "Feature",
                "geometry" : {
                    "type" : "Point",
                    "coordinates" : [37.64, 55.753676]
                },
                "properties" : {
                    "title" : "Крыши24.рф",
                    "placeId" : "roofs24",
                    "detailsUrl" : ".{0}{1}".format(STATIC_URL, 'places/roofs24.json')
                }
            }
        ]
    }

    data = {"places_geojson" : places_geojson}
    
    return render(request, 'index.html', data)

from django.core.management.base import BaseCommand, CommandError
import requests
from django.template.defaultfilters import slugify
from places.models import Place, PlaceImage
from transliterate import translit
from django.core.files.base import ContentFile
import logging
from urllib.parse import urlparse, unquote
import os.path


class Command(BaseCommand):
    help = 'Load json data file to DB'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        loaded_place = response.json()
        place, created = Place.objects.get_or_create(
            title=loaded_place['title'],
            defaults={
                'place_id': slugify(translit(loaded_place['title'][:100], 'ru', reversed=True)),
                'description_short': loaded_place['description_short'],
                'description_long': loaded_place['description_long'],
                'longitude': loaded_place['coordinates']['lng'],
                'latitude': loaded_place['coordinates']['lat'],
            }
        )

    if not created:
        return

    for order, img_url in enumerate(loaded_place['imgs'], 1):
        response = requests.get(img_url)
        response.raise_for_status()

        content_file = ContentFile(response.content)

        place_img = PlaceImage(place=place, order=order)

        url_parts = urlparse(img_url)
        img_path = url_parts.path
        (_, img_name) = os.path.split(img_path)
        img_name = unquote(img_name)

        place_img.image.save(img_name, content_file, True)

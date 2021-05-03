from django.core.management.base import BaseCommand, CommandError
import requests
from django.template.defaultfilters import slugify
from places.models import Place, PlaceImage
from transliterate import translit
from django.core.files.base import ContentFile
import logging


class Command(BaseCommand) :
    help = 'Load json data file to DB'

    def add_arguments(self, parser) :
        parser.add_argument('url', type=str)

    def handle(self, *args, **options) :
        url = options['url']
        try :
            response = requests.get(url)
            response.raise_for_status()
            place_data = response.json()
        except Exception as error :
            logging.error(error)
            return

        place, created = Place.objects.get_or_create(
            title=place_data['title'],
            defaults={
                'place_id' : slugify(translit(place_data['title'][:100], 'ru', reversed=True)),
                'description_short' : place_data['description_short'],
                'description_long' : place_data['description_long'],
                'longitude' : place_data['coordinates']['lng'],
                'latitude' : place_data['coordinates']['lat'],
            }
        )

        if not created :
            return

        for order, img_url in enumerate(place_data['imgs'], 1) :
            try :
                response = requests.get(img_url)
                response.raise_for_status()

                content_file = ContentFile(response.content)

                place_img = PlaceImage(place=place, order=order)

                img_name = img_url.split('/')[-1]
                place_img.image.save(img_name, content_file, True)
            except Exception as error :
                logging.error(error)

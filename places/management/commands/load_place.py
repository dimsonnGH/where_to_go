from django.core.management.base import BaseCommand, CommandError
import requests
from django.template.defaultfilters import slugify
from places.models import Place, PlaceImage
from transliterate import translit
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Load json data file to DB'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)


    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        json = response.json()

        place, created = Place.objects.get_or_create(
            title=json['title'],
            defaults = {
                'placeId': slugify(translit(json['title'][:100], 'ru', reversed=True)),
                'description_short': json['description_short'],
                'description_long': json['description_long'],
                'longitude': json['coordinates']['lng'],
                'latitude': json['coordinates']['lat'],
            }
        )

        if True or created:
            order = 1
            for img_url in json['imgs']:
                response = requests.get(img_url)
                content_file = ContentFile(response.content)

                place_img = PlaceImage()
                place_img.place = place
                place_img.order = order

                img_name = img_url.split('/')[-1]
                place_img.image.save(img_name, content_file, True)

                order += 1





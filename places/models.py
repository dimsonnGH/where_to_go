from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    place_id = models.SlugField(max_length=100, unique=True, verbose_name='Идентификатор')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(blank=True, verbose_name='Подробное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='images')
    image = models.ImageField('Картинка')
    order = models.IntegerField('Порядок', default=0)

    def __str__(self):
        return self.place.title + ' \ ' + self.image.name

    class Meta(object) :
        ordering = ['order']
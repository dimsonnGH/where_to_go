from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=200)
    placeId = models.SlugField(max_length=100, unique=True)
    description_short = models.TextField()
    description_long = HTMLField()
    longitude = models.FloatField()
    latitude = models.FloatField()

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

    class Meta(object) :
        ordering = ['order']
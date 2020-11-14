from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    placeId = models.CharField(max_length=100, unique=True)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Локация',
        related_name='images')
    image = models.ImageField('Картинка')
    order = models.IntegerField('Порядок')

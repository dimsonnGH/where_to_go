# Generated by Django 3.1.1 on 2020-11-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='placeId',
            field=models.CharField(default='placeId', max_length=100),
            preserve_default=False,
        ),
    ]
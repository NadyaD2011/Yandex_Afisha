from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description_short = models.TextField(verbose_name='краткое описание', blank=True)
    description_long = models.TextField(verbose_name='полное описание')
    lat = models.DecimalField(max_digits=50, decimal_places=20, verbose_name='широта')
    lng = models.DecimalField(max_digits=50,  decimal_places=20, verbose_name='долгота')


class Image(models.Model):
    index = models.PositiveIntegerField(default=0, verbose_name='индекс картинки', db_index=True)
    title = models.CharField(max_length=200, verbose_name='название картинки')
    img = models.ImageField(verbose_name='картинка')
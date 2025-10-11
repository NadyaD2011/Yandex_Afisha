from tinymce.models import HTMLField
from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='название', unique=True)
    short_description = models.TextField(verbose_name='краткое описание', blank=True)
    long_description = HTMLField(verbose_name='полное описание', blank=True)
    lat = models.DecimalField(max_digits=50, decimal_places=20, verbose_name='широта')
    lng = models.DecimalField(max_digits=50,  decimal_places=20, verbose_name='долгота')

    def __str__(self) -> str:
        return f'{self.title}'


class Image(models.Model):
    place = models.ForeignKey("Place", on_delete=models.CASCADE, related_name='imgs', verbose_name='место', null=True)
    index = models.PositiveIntegerField(default=0, verbose_name='индекс картинки', db_index=True)
    title = models.CharField(max_length=200, blank=True)
    img = models.ImageField(verbose_name='картинка')

    class Meta:
        ordering = ['index']

    def __str__(self) -> str:
        return f'{self.place}'

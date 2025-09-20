from django.contrib import admin
from .models import Place, Image


@admin.register(Place)
@admin.register(Image)

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)

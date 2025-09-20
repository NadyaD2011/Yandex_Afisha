from django.contrib import admin
from .models import Place, Image


class AdminInline(admin.TabularInline):
    model = Image
    fields = ['img', 'index', 'title']
    verbose_name = 'фотографии'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        AdminInline
    ]

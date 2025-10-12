from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminBase
from django.utils.html import format_html
from django.contrib import admin

from .models import Place, Image


def output_screenshots(obj):
    if obj.img.url:
        return format_html(
            '<img src="{}" style="max-height: 200px; max-width:300px; ">',
            obj.img.url
        )
    return format_html(
        '<span style="color: red;">Ошибка загрузки</span>'
        )


class AdminInline(SortableTabularInline):
    model = Image
    fields = (('img', output_screenshots))
    verbose_name = 'фотографии'
    readonly_fields = [output_screenshots,]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ['place',]
    readonly_fields = [output_screenshots,]
    ordering = ['index']


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    inlines = [
        AdminInline
    ]

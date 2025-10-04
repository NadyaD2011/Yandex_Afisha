from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableAdminBase


def headshot_image(obj):
    try:
        return format_html(
            '<img src="{}" style="max-height: 200px; max-width:300px; ">',
            obj.img.url
        )
    except Exception as error:
        return format_html(
            '<span style="color: red;">Ошибка загрузки</span>'
            )


class AdminInline(SortableTabularInline):
    model = Image
    fields = (('img', headshot_image))
    verbose_name = 'фотографии'
    readonly_fields = [headshot_image,]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    raw_id_fields = ['place',]
    readonly_fields = [headshot_image,]
    ordering = ['index']


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        AdminInline
    ]

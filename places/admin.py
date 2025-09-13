from django.contrib import admin
from places.models import Place

@admin.register(Place)

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
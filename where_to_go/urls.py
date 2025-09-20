from django.contrib import admin
from django.urls import path

from places import views


urlpatterns = [
    path("places/<int:place_id>/", views.parse_place_details, name="parse_place_details"),
    path("admin/", admin.site.urls),
    path('', views.open_map),
]

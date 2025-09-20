from django.contrib import admin
from django.urls import path

from where_to_go import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.open_map),
    path("places/<int:place_id>/", views.parse_place_details, name="parse_place_details"),
]

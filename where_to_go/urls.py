from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

from places import views


urlpatterns = [
    path("places/<int:place_id>/", views.parse_place_details, name="parse_place_details"),
    path("admin/", admin.site.urls),
    path('', views.open_map),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

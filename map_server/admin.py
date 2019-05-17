from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Poster, PosterStatus, PosterType, PosterGroup


@admin.register(Poster)
class PosterAdmin(OSMGeoAdmin):
    default_lat = 6129700
    default_lon = 1288566
    default_zoom = 11
    # Munich:
    # Lat: 48.137222° -> 6129700
    # Lon: 11.575556° -> 1288566


admin.site.register(PosterGroup)
admin.site.register(PosterStatus)
admin.site.register(PosterType)

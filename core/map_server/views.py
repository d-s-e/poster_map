from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_gis.filters import InBBoxFilter

from map_server.serializers import PosterSerializer
from map_server.models import Poster


class PosterView(ListView):
    queryset = Poster.objects.all()


class PosterViewSet(ReadOnlyModelViewSet):
    bbox_filter_field = "position"
    filter_backends = (InBBoxFilter,)
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

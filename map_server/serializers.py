from rest_framework.serializers import ModelSerializer, StringRelatedField
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from map_server.models import Poster, PosterStatus, PosterType


class PosterStatusSerializer(ModelSerializer):
    class Meta:
        model = PosterStatus
        fields = ("name", "label",)


class PosterTypeSerializer(ModelSerializer):
    class Meta:
        model = PosterType
        fields = ("name", "label",)


class PosterSerializer(GeoFeatureModelSerializer):
    status = PosterStatusSerializer(read_only=True)
    poster_type = PosterTypeSerializer(read_only=True)

    class Meta:
        model = Poster
        geo_field = "position"
        fields = ("status", "poster_type", "comment", "last_modified",)

from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class PosterType(models.Model):
    """the current type or theme of a poster"""
    name = models.CharField(max_length=20, unique=True, blank=False)
    label = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.label


class PosterStatus(models.Model):
    """the current status of a poster, like ok, broken, missing, ..."""
    name = models.CharField(max_length=50, unique=True, blank=False)
    label = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.label


class PosterGroup(models.Model):
    """a specific group that is responsible for a certain area"""
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.TextField(max_length=200, blank=True)
    admins = models.ManyToManyField(User, related_name="group_admin")
    members = models.ManyToManyField(User, related_name="group_member")
    poster_types = models.ManyToManyField(PosterType)
    bounding_box = models.PolygonField(null=True, geography=True)

    def __str__(self):
        return self.name


class Poster(models.Model):
    """a specific poster or group of posters standing somewhere"""
    user = models.ForeignKey(User, null=False, related_name="posters", on_delete=models.PROTECT)
    group = models.ForeignKey(PosterGroup, null=True, on_delete=models.PROTECT)
    status = models.ForeignKey(PosterStatus, null=False, related_name="posters", on_delete=models.PROTECT)
    poster_type = models.ForeignKey(PosterType, null=True, related_name="posters", on_delete=models.PROTECT)
    comment = models.TextField(blank=True, max_length=500)
    position = models.PointField(null=False, geography=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def coords_lat_lon(self):
        return tuple(self.position[::-1])

    def __str__(self):
        return "{:%d.%m.%Y %H:%M}: {} [{}] - {}".format(self.last_modified, self.group, self.status, self.coords_lat_lon)

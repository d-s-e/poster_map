#!/usr/bin/env python

from django.contrib.auth.models import User
from django.contrib.gis.gdal import DataSource
from map_server.models import PosterStatus, PosterGroup, PosterType, Poster


user = User.objects.first()


def import_data(gpx_source_file, poster_type="unknown", poster_status="ok"):
    status = PosterStatus.objects.get(name=poster_status)
    ptype = PosterType.objects.get(name=poster_type)

    data = DataSource(gpx_source_file)
    wp = data[0]

    for p in wp:
        print(p["name"], p["type"], p.geom)
        pst = Poster()
        pst.comment = "type: {}\nstatus: {}\n\nname: {}".format(p["type"], p["status"], p["name"])
        pst.user = user
        pst.status = status
        pst.poster_type = ptype
        pst.position = p.geom.geos
        pst.save()


file = "~/Projekte/pirate-tools-2019/Plakatierung/Standorte_Muenchen_A0_Hohlkammer_EU.gpx"
import_data(file, "eu_hk_a0")


file = "~/Projekte/pirate-tools-2019/Plakatierung/Standorte_Muenchen_EU.gpx"
import_data(file, "eu_af_a0")


file = "~/Projekte/pirate-tools-2019/Plakatierung/Standorte_Muenchen_alt.gpx"
import_data(file, "muc_alt_a0")


file = "~/Projekte/pirate-tools-2019/Plakatierung/Standorte_Muenchen_ungeprueft.gpx"
import_data(file, "unknown", "unknown")

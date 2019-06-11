from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from map_server.views import PosterView, PosterViewSet


router = DefaultRouter()
router.register(r"posters", PosterViewSet, basename="posters")


urlpatterns = [
    path('', PosterView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

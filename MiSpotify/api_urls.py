from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

from modules.Album.api.views import AlbumViewSet


router = DefaultRouter()
router.register(r'albums',AlbumViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
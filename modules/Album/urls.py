from django.conf.urls import url,include
from .views import (
                    AlbumCreate, 
                    AlbumUpdate, 
                    AlbumDelete,
                    AlbumDetailView,
                    AlbumListView,
                    manage_song
                    )
 
 
urlpatterns = [
    url(r'^$', AlbumListView.as_view(), name='album-list'),
    url(r'^(?P<pk>[0-9]+)/$', AlbumDetailView.as_view(), name='album-detail'),
    url(r'^add/$', AlbumCreate.as_view(), name='album-add'),
    url(r'^(?P<pk>[0-9]+)/update$', AlbumUpdate.as_view(), name='album-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', AlbumDelete.as_view(), name='album-delete'),
    url(r'^(?P<pk>[0-9]+)/manage/$',manage_song, name='album-manage'),
]
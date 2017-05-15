from django.conf.urls import url,include
from .views import (
                    SongCreate, 
                    SongUpdate, 
                    SongDelete,
                    SongDetailView,
                    SongListView,
                    manage_playlist,
                    )
 
urlpatterns = [
    url(r'^$', SongListView.as_view(), name='song-list'),
    url(r'^(?P<pk>[0-9]+)/$', SongDetailView.as_view(), name='song-detail'),
    url(r'^add/$', SongCreate.as_view(), name='song-add'),
    url(r'^(?P<pk>[0-9]+)/update$', SongUpdate.as_view(), name='song-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', SongDelete.as_view(), name='song-delete'),
    url(r'^(?P<pk>[0-9]+)/manage/$', manage_playlist, name='song-manage'),
]
from django.conf.urls import url,include
from .views import (
                    PlaylistCreate, 
                    PlaylistUpdate, 
                    PlaylistDelete,
                    PlaylistDetailView,
                    PlaylistListView
                    )
 
urlpatterns = [
    url(r'^$', PlaylistListView.as_view(), name='playlist-list'),
    url(r'^(?P<pk>[0-9]+)/$', PlaylistDetailView.as_view(), name='playlist-detail'),
    url(r'^add/$', PlaylistCreate.as_view(), name='playlist-add'),
    url(r'^(?P<pk>[0-9]+)/update$', PlaylistUpdate.as_view(), name='playlist-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PlaylistDelete.as_view(), name='playlist-delete'),
]
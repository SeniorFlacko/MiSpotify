from django.conf.urls import url,include
from .views import (
                    ArtistCreate, 
                    ArtistUpdate, 
                    ArtistDelete,
                    ArtistDetailView,
                    ArtistListView
                    )
 
urlpatterns = [
    url(r'^$', ArtistListView.as_view(), name='artist-list'),
    url(r'^(?P<pk>[0-9]+)/$', ArtistDetailView.as_view(), name='artist-detail'),
    url(r'^add/$', ArtistCreate.as_view(), name='artist-add'),
    url(r'^(?P<pk>[0-9]+)/update$', ArtistUpdate.as_view(), name='artist-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', ArtistDelete.as_view(), name='artist-delete'),
]
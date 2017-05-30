from rest_framework.serializers import HyperlinkedModelSerializer,HyperlinkedRelatedField

from ..models import Album

class AlbumSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('url','title','artist')
        extra_kwargs = {
            'artist': {'view_name': 'artist:artist-detail'},
        }
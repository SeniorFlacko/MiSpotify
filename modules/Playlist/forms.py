from django.forms import ModelForm
from .models import Playlist_Song
class Playlist_SongForm(ModelForm):
    class Meta:
        model = Playlist_Song
        fields = '__all__'
from django.db import models

# Create your models here.
from django.urls import reverse
from django.conf import settings

from modules.Song.models import Song
class Playlist(models.Model):
    name = models.CharField(max_length=120)
    made_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    create_reason = models.CharField(max_length=64,default=" ")
    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return reverse('playlist:playlist-detail', kwargs={'pk': self.pk})


class Playlist_Song(models.Model):
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    

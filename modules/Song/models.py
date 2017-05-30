from django.db import models

# Create your models here.
from django.urls import reverse
from modules.Album.models import Album

class Song(models.Model):
    title = models.CharField(max_length=120)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse('song:song-detail', kwargs={'pk': self.pk})

class LP(models.Model):
    title = models.CharField(max_length=120)
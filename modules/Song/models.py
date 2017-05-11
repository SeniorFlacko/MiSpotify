# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse
from modules.Album.models import Album

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)



    def __str__(self):
        return "%s" % (self.song_title)

    def get_absolute_url(self):
        return reverse('song-detail', kwargs={'pk': self.pk})

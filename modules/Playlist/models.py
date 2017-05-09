# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse

class Playlist(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return reverse('playlist-detail', kwargs={'pk': self.pk})
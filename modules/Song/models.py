# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.urls import reverse

class Song(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse('song-detail', kwargs={'pk': self.pk})
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse('album-detail', kwargs={'pk': self.pk})
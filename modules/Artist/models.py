from django.db import models

# Create your models here.

from django.urls import reverse
class Artist(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return "%s" % (self.name)

    def get_absolute_url(self):
        return reverse('artist:artist-detail', kwargs={'pk': self.pk})

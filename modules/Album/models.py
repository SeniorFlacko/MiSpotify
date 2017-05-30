from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.
from django.urls import reverse
from modules.Artist.models import Artist
from modules.Comment.models import Comment
# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=120)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    comments = GenericRelation(Comment)

    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse('album:album-detail', kwargs={'pk': self.pk})


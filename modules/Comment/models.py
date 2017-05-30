from django.db import models

# Create your models here.

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    comm = models.CharField(max_length=50)

    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "%s" % (self.comm)

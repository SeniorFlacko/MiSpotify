# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Playlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist_song',
            name='create_reason',
        ),
        migrations.AddField(
            model_name='playlist',
            name='create_reason',
            field=models.CharField(default=' ', max_length=64),
        ),
    ]
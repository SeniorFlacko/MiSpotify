# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Playlist', '0002_auto_20170513_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist_song',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
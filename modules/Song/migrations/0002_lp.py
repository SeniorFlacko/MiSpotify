# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
    ]

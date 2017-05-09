# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Song

class SongCreate(CreateView):
    model = Song
    fields = ['title']

class SongUpdate(UpdateView):
    model = Song
    fields = ['title']
    template_name_suffix = '_update_form'

class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('song-list')

class SongDetailView(DetailView):
    model = Song

class SongListView(ListView):
    model = Song
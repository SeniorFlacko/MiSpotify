# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Playlist

class PlaylistCreate(CreateView):
    model = Playlist
    fields = ['name']

class PlaylistUpdate(UpdateView):
    model = Playlist
    fields = ['name']
    template_name_suffix = '_update_form'

class PlaylistDelete(DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlist-list')

class PlaylistDetailView(DetailView):
    model = Playlist

class PlaylistListView(ListView):
    model = Playlist
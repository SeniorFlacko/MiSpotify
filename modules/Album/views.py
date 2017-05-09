# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Album

class AlbumCreate(CreateView):
    model = Album
    fields = ['title']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['title']
    template_name_suffix = '_update_form'

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('album-list')

class AlbumDetailView(DetailView):
    model = Album

class AlbumListView(ListView):
    model = Album
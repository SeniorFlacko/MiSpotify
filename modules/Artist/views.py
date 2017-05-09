# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Artist

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name']

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name']
    template_name_suffix = '_update_form'

class ArtistDelete(DeleteView):
    model = Artist
    success_url = reverse_lazy('artist-list')

class ArtistDetailView(DetailView):
    model = Artist

class ArtistListView(ListView):
    model = Artist
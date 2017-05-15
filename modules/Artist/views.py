from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Artist

from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory

from modules.Album.models import Album

class ArtistCreate(CreateView):
    model = Artist
    fields = '__all__'

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


def manage_albums(request, pk):
    artist = Artist.objects.get(pk=pk)
    name = artist.name
    AlbumInlineFormSet = inlineformset_factory(Artist, Album, fields=('title',))
    if request.method == "POST":
        formset = AlbumInlineFormSet(request.POST, request.FILES, instance=artist)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(artist.get_absolute_url())
    else:
        formset = AlbumInlineFormSet(instance=artist)
    return render(request, 'Artist/manage_albums.html', {'formset': formset,'name':name})
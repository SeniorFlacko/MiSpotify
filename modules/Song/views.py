from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Song
from django.http import HttpResponseRedirect
from modules.Playlist.models import Playlist_Song
from django.forms import inlineformset_factory

class SongCreate(CreateView):
    model = Song
    fields = '__all__'

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

def manage_playlist(request, pk):
    song = Song.objects.get(pk=pk)
    title = song.title
    PlaylistInlineFormSet = inlineformset_factory(Song, Playlist_Song, fields=('playlist',))
    if request.method == "POST":
        formset = PlaylistInlineFormSet(request.POST, request.FILES, instance=song)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(song.get_absolute_url())
    else:
        formset = PlaylistInlineFormSet(instance=song)
    return render(request, 'Song/manage_playlist.html', {'formset': formset,'title':title})
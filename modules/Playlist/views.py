from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Playlist,Playlist_Song
from django.http import HttpResponseRedirect
from modules.Song.models import Song
from django.forms import inlineformset_factory
class PlaylistCreate(CreateView):
    model = Playlist
    fields = '__all__'

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


def manage_song(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    name = playlist.name
    SongInlineFormSet = inlineformset_factory(Playlist, Playlist_Song, fields=('song',))
    if request.method == "POST":
        formset = SongInlineFormSet(request.POST, request.FILES, instance=playlist)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(playlist.get_absolute_url())
    else:
        formset = SongInlineFormSet(instance=playlist)
    return render(request, 'Playlist/manage_songs.html', {'formset': formset,'name':name})
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Album
from django.http import HttpResponseRedirect
from modules.Song.models import Song
from django.forms import inlineformset_factory
class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'

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

def manage_song(request, pk):
    album = Album.objects.get(pk=pk)
    title = album.title
    SongInlineFormSet = inlineformset_factory(Album, Song, fields=('title',))
    if request.method == "POST":
        formset = SongInlineFormSet(request.POST, request.FILES, instance=album)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(album.get_absolute_url())
    else:
        formset = SongInlineFormSet(instance=album)
    return render(request, 'Album/manage_songs.html', {'formset': formset,'title':title})
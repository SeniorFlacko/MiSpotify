from django.contrib import admin

# Register your models here.
from .models import Song
from modules.Playlist.models import Playlist_Song

class Playlist_SongInline(admin.TabularInline):
    model = Playlist_Song

class SongAdmin(admin.ModelAdmin):
    inlines = (Playlist_SongInline,)

admin.site.register(Song,SongAdmin)

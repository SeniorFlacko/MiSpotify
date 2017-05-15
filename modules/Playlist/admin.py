from django.contrib import admin

# Register your models here.
from .models import Playlist_Song,Playlist
class Playlist_SongInline(admin.TabularInline):
    model = Playlist_Song

class PlaylistAdmin(admin.ModelAdmin):
    inlines = (Playlist_SongInline,)


admin.site.register(Playlist,PlaylistAdmin)
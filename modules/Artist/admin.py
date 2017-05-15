from django.contrib import admin

# Register your models here.
from .models import Artist
from modules.Album.models import Album

class AlbumInline(admin.TabularInline):
    model = Album
    
class ArtistAdmin(admin.ModelAdmin):
    inlines = (AlbumInline,)

admin.site.register(Artist,ArtistAdmin)

from django.contrib import admin

# Register your models here.
from .models import User
from modules.Playlist.models import Playlist

class PlaylistInline(admin.TabularInline):
    model = Playlist
    
class UserAdmin(admin.ModelAdmin):
    inlines = (PlaylistInline,)
    fields = ('username','date_joined','bio','email','country','birth_date',)
admin.site.register(User,UserAdmin)
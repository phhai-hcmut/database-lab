from django.contrib import admin

from .models import Playlist, PlaylistContent


admin.site.register(Playlist)
admin.site.register(PlaylistContent)

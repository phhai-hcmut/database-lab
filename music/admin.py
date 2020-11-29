from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Credit)
admin.site.register(User)
# admin.site.register(Playlist)
# admin.site.register(PlaylistContent)
admin.site.register(QueueTrack)
admin.site.register(CurrentlyListening)

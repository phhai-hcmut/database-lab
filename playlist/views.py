from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Playlist


@login_required
def index(request):
    """Render a list of user's playlists"""
    # TODO: link to templates
    return HttpResponse("A list of user's playlists")


def detail(request, pk):
    """Render a list of tracks in the playlist"""
    # TODO: link to templates
    playlist = Playlist.objects.get(pk=pk)
    if not playlist.is_public and request.user != playlist.user:
        resp = HttpResponse("Private playlist", status=401)
    else:
        resp = HttpResponse("A list of tracks in the playlist")
    return render(request, 'music/playlist_detail.html', {'playlist': playlist})

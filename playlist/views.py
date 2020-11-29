from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Render a list of user's playlists"""
    return HttpResponse("A list of user's playlists")


def detail(request, pk):
    """Render a list of tracks in the playlist"""
    return HttpResponse("A list of tracks in the playlist")

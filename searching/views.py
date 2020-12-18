from listening.models import InQueue
from django.shortcuts import render

# Create your views here.
from music.models import *
from playlist.models import *
# ___________________________SEARCH VIEWS__________________________
from django.views.generic import TemplateView, ListView
from django.db.models import Q


def searchView(request):
    return render(request, 'structure/navbar.html', None)

class QueryHolder:
    def __init__(self,query_str) -> None:
        self.value = query_str
class SearchResultView(ListView):
    template_name = 'searching/search_result.html'
    context_object_name = 'result'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        albums = Album.objects.filter(
            Q(name__icontains=query)
        )
        playlist_query = Q(is_public=True)
        if self.request.user.is_authenticated:
            playlist_query = playlist_query | Q(user=self.request.user)
        playlists = Playlist.objects.filter(
            Q(name__icontains=query), playlist_query
        )
        artists = Artist.objects.filter(
            Q(name__icontains=query)
        )
        tracks = Track.objects.filter(
            Q(recording__name__icontains=query)
        )
        result = {'albums': albums, 'playlists': playlists, 'artists': artists, 'tracks': tracks, 'query' : query}
        return result


def searchArtist(request,query):
    playlist_list = Artist.objects.filter(
            Q(name__icontains=query)
        )
    in_queue = InQueue.objects.filter(user = request.user).order_by('queue_index')
    # TODO: link html file
    return render(request, 'searching/list_page/artist_list.html', {'artist_list': playlist_list,
                                                                  'in_queue': in_queue})
                                                                
def searchAlbum(request,query):
    playlist_list = Album.objects.filter(
            Q(name__icontains=query)
        )
    in_queue = InQueue.objects.filter(user = request.user).order_by('queue_index')
    # TODO: link html file
    return render(request, 'searching/list_page/album_list.html', {'album_list': playlist_list,
                                                                  'in_queue': in_queue})
def searchTrack(request,query):
    playlist_list = Track.objects.filter(
            Q(recording__name__icontains=query)
        )
    in_queue = InQueue.objects.filter(user = request.user).order_by('queue_index')
    # TODO: link html file
    return render(request, 'searching/list_page/track_list.html', {'track_list': playlist_list,
                                                                  'in_queue': in_queue})
def searchPlaylist(request,query):
    playlist_query = Q(is_public=True)
    if request.user.is_authenticated:
        playlist_query = playlist_query | Q(user=request.user)
    playlist_list = Playlist.objects.filter(
        Q(name__icontains=query), playlist_query
    )
    in_queue = InQueue.objects.filter(user = request.user).order_by('queue_index')
    # TODO: link html file
    return render(request, 'searching/list_page/playlist_list.html', {'playlist_list': playlist_list,
                                                                  'in_queue': in_queue})
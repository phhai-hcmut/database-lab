from django.views.generic import TemplateView, ListView

# Create your views here.
from listening.models import InQueue
from music.models import Artist, Album, Track
from playlist.models import Playlist


class SearchResultView(TemplateView):
    template_name = 'searching/search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        context['albums'] = Album.objects.filter(
            name__icontains=query
        )
        context['playlists'] = Playlist.objects.visible(self.request.user).filter(
            name__icontains=query
        )
        context['artists'] = Artist.objects.filter(
            name__icontains=query
        )
        context['tracks'] = Track.objects.filter(
            recording__name__icontains=query
        )
        return context


class SearchArtistView(ListView):
    template_name = 'searching/list_page/artist_list.html'

    def get_queryset(self):
        query = self.kwargs['query']
        return Artist.objects.filter(name__icontains=query)


class SearchAlbumView(ListView):
    template_name = 'searching/list_page/album_list.html'

    def get_queryset(self):
        search_query = self.kwargs['query']
        queryset = Album.objects.filter(name__icontains=search_query)
        return queryset

# def searchTrack(request,query):
#     playlist_list = Track.objects.filter(
#             Q(recording__name__icontains=query)
#         )
#     in_queue = InQueue.objects.filter(user = request.user).order_by('queue_index')
#     # TODO: link html file
#     return render(request, 'searching/list_page/track_list.html', {'track_list': playlist_list,


class SearchPlaylistView(ListView):
    template_name = 'searching/list_page/playlist_list.html'

    def get_queryset(self):
        search_query = self.kwargs['query']
        queryset = Playlist.objects.visible(self.request.user).filter(name__icontains=search_query)
        return queryset

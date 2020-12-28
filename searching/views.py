from django.views.generic import TemplateView, ListView

# Create your views here.
from listening.models import InQueue
from music.models import Artist, Album, Recording
from playlist.models import Playlist


class SearchResultView(TemplateView):
    template_name = 'searching/search_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        context['albums'] = Album.objects.filter(name__icontains=query)
        context['playlists'] = Playlist.objects.visible(self.request.user).filter(
            name__icontains=query
        )
        context['artists'] = Artist.objects.filter(name__icontains=query)
        context['recordings'] = Recording.objects.filter(name__icontains=query)
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


class SearchRecordingView(ListView):
    template_name = 'searching/list_page/recording_list.html'

    def get_queryset(self):
        search_query = self.kwargs['query']
        queryset = Recording.objects.filter(name__icontains=search_query)
        return queryset


class SearchPlaylistView(ListView):
    template_name = 'searching/list_page/playlist_list.html'

    def get_queryset(self):
        search_query = self.kwargs['query']
        queryset = Playlist.objects.visible(self.request.user).filter(
            name__icontains=search_query
        )
        return queryset

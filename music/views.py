from django.views.generic.base import TemplateView
from listening.models import InQueue
from playlist.models import Playlist

from .models import Album, Artist, Credit, Recording, Track

# Create your views here.


# ____________________________LISTENER VIEWS__________________________

class AlbumDetail:
    def __init__(self, album):
        self.name = album.name
        self.release_date = album.release_date
        self.album_type = album.album_type
        self.track_list = album.track.all()
        self.owner_list = album.owner.distinct()


class ArtistDetail:
    def __init__(self, artist):
        self.name = artist.name
        self.owned_albums = artist.album.all()
        self.credited_recording = artist.artist_credit.all()
        self.credited_tracks = Track.objects.filter(recording__in=self.credited_recording)


class TrackDetail:
    def __init__(self, track):
        self.name = track.recording.name
        self.track_number = track.track_number
        self.duration = track.recording.duration
        self.credit = Credit.objects.filter(recording=track.recording)
        self.album = track.album


class AlbumSummary(AlbumDetail):
    max_owners_shown = 5
    max_tracks_shown = 3

    def __init__(self, album):
        super().__init__(album)
        self.owner_list = self.owner_list[:self.max_owners_shown]
        self.track_list = self.track_list[: self.max_tracks_shown]


class ArtistSummary(ArtistDetail):
    max_albums_shown = 5
    max_credits_shown = 3

    def __init__(self, album):
        super().__init__(album)
        self.owned_albums = self.owned_albums[:self.max_albums_shown]
        self.credit_list = self.credit_list[: self.max_credits_shown]


class TrackSummary(TrackDetail):
    max_credits_shown = 5
    max_albums_shown = 3

    def __init__(self, album):
        super().__init__(album)
        self.credit_list = self.credit_list[:self.max_credits_shown]
        self.albums = self.albums[: self.max_albums_shown]


class HomePageView(TemplateView):
    """Render only top track/artist/album for homepage compact display"""
    TOP_NUMBER = 5
    template_name = 'music/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_album_list'] = Album.objects.all()[:self.TOP_NUMBER]
        context['top_artist_list'] = Artist.objects.all()[:self.TOP_NUMBER]
        context['top_playlist'] = Playlist.objects.visible(self.request.user).order_by('-time_created')[:self.TOP_NUMBER]
        return context

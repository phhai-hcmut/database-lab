from listening.models import InQueue
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from dataclasses import dataclass
from django.http import HttpResponse
# Create your views here.

from music.models import Album, Artist, Credit, Recording, Track
from playlist.models import Playlist
from listening.models import InQueue


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
        self.credited_tracks = Track.objects.filter(recording__in = self.credited_recording)


class TrackDetail:
    def __init__(self, track):
        self.name = track.recording.name
        self.track_number = track.track_number
        self.duration = track.recording.duration
        self.credit = Credit.objects.filter(recording = track.recording)
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


# NOTE: function for getting detailed page of album/artist/track
def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    album_detail = AlbumDetail(album)
    in_queue = InQueue.objects.order_by('queue_index')
    return render(request, 'music/album_detail.html', {'album': album_detail,
                                                       'in_queue': in_queue})


def track_detail(request, pk):
    track = Track.objects.get(pk=pk)
    track_detail = TrackDetail(track)
    in_queue = InQueue.objects.order_by('queue_index')
    return render(request, 'music/track_detail.html', {'track': track_detail,
                                                       'in_queue': in_queue})


def artist_detail(request, pk):
    artist = Artist.objects.get(pk=pk)
    artist_detail = ArtistDetail(artist)
    in_queue = InQueue.objects.order_by('queue_index')
    return render(request, 'music/artist_detail.html', {'artist': artist_detail,
                                                        'in_queue': in_queue})


# NOTE: function for getting full list track/artist/album for gallery view
def album_list(request):
    album_list = Album.objects.order_by('-release_date').all()
    in_queue = InQueue.objects.order_by('queue_index')
    return render(request, 'music/list_page/album_list.html', {'album_list': album_list,
                                                               'in_queue': in_queue})


def track_list(request):
    track_list = Track.objects.order_by('track_number').all()
    in_queue = InQueue.objects.order_by('queue_index')
    # TODO: link html file
    return render(request, 'music/list_page/track_list.html', {'track_list': track_list,
                                                               'in_queue': in_queue})


def artist_list(request):
    artist_list = Artist.objects.order_by('name').all()
    in_queue = InQueue.objects.order_by('queue_index')
    # TODO: link html file
    return render(request, 'music/list_page/artist_list.html', {'artist_list': artist_list,
                                                                'in_queue': in_queue})

def playlist_list(request):
    playlist_list = Playlist.objects.order_by('name').all()
    in_queue = InQueue.objects.order_by('queue_index')
    # TODO: link html file
    return render(request, 'music/list_page/playlist_list.html', {'playlist_list': playlist_list,
                                                                  'in_queue': in_queue})

# NOTE: function to get only top track/artist/album for homepage compact display
TOP_NUMBER = 5
def detail(request):
    # return HttpResponse("You're looking at album  %s." % album_id)
    return render(request, 'music/album_detail.html')


def index(request):
    all_album_list = Album.objects.order_by('-release_date')[:TOP_NUMBER]
    top_track_list = Track.objects.order_by('track_number')[:TOP_NUMBER]
    top_artist_list = Artist.objects.order_by('name')[:TOP_NUMBER]
    top_playlist = Playlist.objects.order_by('-time_created')[:TOP_NUMBER]
    in_queue = InQueue.objects.order_by('queue_index')
    context = {'all_album_list': all_album_list,
               'top_track_list': top_track_list,
               'top_artist_list': top_artist_list,
               'top_playlist': top_playlist,
               'in_queue': in_queue}
    return render(request, 'music/index.html', context)


def all_albums(request):
    album_list = Album.objects.order_by('-release_date')[:TOP_NUMBER]
    album_summary_list = [AlbumSummary(album) for album in album_list]
    artist_list = Artist.objects.order_by('-name')[:TOP_NUMBER]
    artist_summary_list = [ArtistSummary(artist) for artist in artist_list]
    # TODO: link html file
    return render(request, 'music/index.html', {'album_list': album_summary_list,
                                                'artist_list': artist_summary_list})


def all_tracks(request):
    track_list = Track.objects.order_by('-duration')[:TOP_NUMBER]
    track_summary_list = [TrackSummary(track) for track in track_list]
    # TODO: link html file
    return render(request, 'HTML?', {'track_list': track_summary_list})


def all_artists(request):
    artist_list = Artist.objects.order_by('-name')[:TOP_NUMBER]
    artist_summary_list = [ArtistSummary(artist) for artist in artist_list]
    # TODO: link html file
    return render(request, 'HTML?', {'artist_list': artist_summary_list})


# NOTE: Helper function lower level
def album_owner(album):
    return album.artist.all()


def album_track(album):
    return album.track.all()


def track_credit(track):
    return track.artist_credit.all()


def track_album(track):
    return track.album.all()


def artist_track(artist):
    return artist.track.all()


def artist_album(artist):
    return artist.album.all()

# ____________________________ARTIST VIEWS__________________________


# ____________________________MODERATOR VIEWS__________________________
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def addMusic(request):
    if request.is_ajax():
        track_id = request.POST.get('id',None)
        user_id = request.user.id
        print('user id:',user_id,'track: ',track_id)
        #find the recording
        recording = Track.objects.get(pk = track_id).recording
        user = request.user
        if not InQueue.objects.filter(user = user):
            InQueue.objects.create(user = user, recording = recording, queue_index = 1)
        else:
            last_queued = InQueue.objects.filter(user = user).last()
            InQueue.objects.create(user = user, recording = recording, queue_index = last_queued.queue_index + 1)
    else:
        print('no')
    return HttpResponse('Updated')

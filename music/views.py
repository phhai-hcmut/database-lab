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

from music.models import Album, Artist, Track, Playlist




# ____________________________LISTENER VIEWS__________________________

class AlbumDetail:
    def __init__(self, album):
        self.name = album.name
        self.release_date = album.release_date
        self.album_type = album.album_type
        self.track_list = album.track.all()
        self.owner_list = album.owner.all()


class ArtistDetail:
    def __init__(self, artist):
        self.name = artist.name
        self.owned_albums = artist.album.all()
        self.credit_list = artist.track.all()


class TrackDetail:
    def __init__(self, track):
        self.name = track.name
        self.track_number = track.track_number
        self.duration = track.duration
        self.artist_credit = track.artist_credit.all()
        self.albums = track.album.all()


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
def album_detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    album_detail = AlbumDetail(album)
    # TODO: link html file
    return render(request, 'HTML?', {'album': album_detail})


def track_detail(request, track_id):
    track = Track.objects.get(pk=track_id)
    track_detail = TrackDetail(track)
    # TODO: link html file
    return render(request, 'HTML?', {'track': TrackDetail})


def artist_detail(request, artist_id):
    artist = Artist.objects.get(pk=artist_id)
    artist_detail = ArtistDetail(artist)
    # TODO: link html file
    return render(request, 'HTML?', {'artist': artist_detail})


# NOTE: function for getting full list track/artist/album for gallery view
# def all_albums(request):
#     album_list = Album.objects.all()
#     album_summary_list = [AlbumSummary(album) for album in album_list]
#     return render(request, 'HTML?', {'album_list': album_summary_list})
#
#
# def all_tracks(request):
#     track_list = Track.objects.all()
#     track_summary_list = [TrackSummary(track) for track in track_list]
#     # TODO: link html file
#     return render(request, 'HTML?', {'track_list': track_summary_list})
#
#
# def all_artists(request):
#     artist_list = Artist.objects.all()
#     artist_summary_list = [ArtistSummary(artist) for artist in artist_list]
#     # TODO: link html file
#     return render(request, 'HTML?', {'artist_list': artist_summary_list})


# NOTE: function to get only top track/artist/album for homepage compact display
TOP_NUMBER = 5


# def all_albums(request):
#     album_list = Album.objects.order_by('-release_date')[:TOP_NUMBER]
#     album_summary_list = [AlbumSummary(album) for album in album_list]
#     # TODO: link html file
#     return render(request, 'HTML?', {'album_list': album_summary_list})

def detail(request):
    # return HttpResponse("You're looking at album  %s." % album_id)
    return render(request, 'music/album_detail.html')


def index(request):
    all_album_list = Album.objects.order_by('-release_date')[:TOP_NUMBER]
    top_track_list = Track.objects.order_by('name')[:TOP_NUMBER]
    top_artist_list = Artist.objects.order_by('name')[:TOP_NUMBER]
    top_playlist = Playlist.objects.order_by('-time_created')[:TOP_NUMBER]
    context = {'all_album_list': all_album_list,
               'top_track_list': top_track_list,
               'top_artist_list': top_artist_list,
               'top_playlist': top_playlist}
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

from music.models import Album, Artist, Track
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


#NOTE: function for getting detailed page of album/artist/track
def album_detail(request,album_id):
    album = Album.objects.get(pk = album_id)
    #TODO: link html file
    return render(request, 'HTML?', {'album': album})
def track_detail(request,track_id):
    track = Track.objects.get(pk = track_id)
    #TODO: link html file
    return render(request, 'HTML?', {'track': track})
def artist_detail(request,artist_id):
    artist = Artist.objects.get(pk = artist_id)
    #TODO: link html file
    return render(request, 'HTML?', {'artist': artist})

#NOTE: function for getting full list track/artist/album for gallery view
def all_albums(request):
    album_list = Album.objects.all()
    #TODO: link html file
    return render(request, 'HTML?', {'album_list': album_list})
def all_tracks(request):
    track_list = Track.objects.all()
    #TODO: link html file
    return render(request, 'HTML?', {'track_list': track_list})
def all_artists(request):
    artist_list = Artist.objects.all()
    #TODO: link html file
    return render(request, 'HTML?', {'artist_list': artist_list})

#NOTE: function to get only top track/artist/album for homepage compact display
TOP_NUMBER = 5
def all_albums(request):
    album_list = Album.objects.order_by('-release_date')[:TOP_NUMBER]
    #TODO: link html file
    return render(request, 'HTML?', {'album_list': album_list})
def all_tracks(request):
    track_list = Track.objects.order_by('-duration')[:TOP_NUMBER]
    #TODO: link html file
    return render(request, 'HTML?', {'track_list': track_list})
def all_artists(request):
    artist_list = Artist.objects.order_by('-name')[:TOP_NUMBER]
    #TODO: link html file
    return render(request, 'HTML?', {'artist_list': artist_list})

#NOTE: 
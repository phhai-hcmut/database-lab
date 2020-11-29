from music.models import Album
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    all_album_list = Album.objects.order_by('-name')
    context = {'all_album_list': all_album_list}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    return HttpResponse("You're looking at album  %s." % album_id)
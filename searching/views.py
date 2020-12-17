from django.shortcuts import render

# Create your views here.
from music.models import *
from playlist.models import *
# ___________________________SEARCH VIEWS__________________________
from django.views.generic import TemplateView, ListView
from django.db.models import Q 
def searchView(request):
    return render(request, 'searching/search.html',None)
class SearchResultView(ListView):
    template_name = 'searching/search_result.html'
    context_object_name = 'result'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        albums = Album.objects.filter(
            Q(name__icontains=query)
        )
        playlists = Playlist.objects.filter(
            Q(name__icontains=query)
        )   
        artists = Artist.objects.filter(
            Q(name__icontains=query)
        )   
        tracks = Track.objects.filter(
            Q(recording__name__icontains=query)
        )
        
        result = {'albums': albums, 'playlists': playlists, 'artists': artists, 'tracks': tracks}
        return result
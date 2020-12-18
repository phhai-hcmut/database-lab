from pprint import pformat

from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.forms import formset_factory, ModelForm, modelform_factory, inlineformset_factory
from django.http import HttpResponse

from music.models import Album, Artist, Credit, Recording, Track

# Create your views here.
class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'


class AlbumUpdate(UpdateView):
    model = Album
    fields = '__all__'


class AlbumDelete(DeleteView):
    model = Album
    template_name = 'music/album_form.html'
    success_url = reverse_lazy('music:index')
    fields = '__all__'


AlbumForm = modelform_factory(Album, fields='__all__')


class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['track_number', 'recording']


# TrackFormSet = formset_factory(TrackForm, extra=1)
TrackFormSet = inlineformset_factory(Album, Track, fields=('track_number', 'recording'), extra=1)


def album_create(request):
    if request.method == 'POST':
        album = AlbumForm(request.POST)
        tracks = TrackFormSet(request.POST)
        if tracks.is_valid():
            resp = HttpResponse(tracks[0].cleaned_data['album'])
    else:
        form = {'album_form': AlbumForm(), 'track_formset': TrackFormSet(initial=[{'track_number':1}])}
        resp = render(request, 'edit/album_form.html', form)
    return resp


def album_update(request, pk):
    if request.method == 'POST':
        album = AlbumForm(request.POST)
        tracks = TrackFormSet(request.POST)
        if album.is_valid() and tracks.is_valid():
            album.save()
            tracks.save()
            resp = HttpResponse("OK")
        else:
            resp = HttpResponse("Error")
    else:
        album = Album.objects.get(pk=pk)
        form = {'album_form': AlbumForm(instance=album), 'track_formset': TrackFormSet(instance=album)}
        resp = render(request, 'edit/album_form.html', form)
    return resp


# def album_delete(request, pk):
#     album = Album.objects.get(pk=pk)
#     if request.method == 'POST':
#         album.delete()
#         resp = HttpResponse("OK")
#     else:
#         resp = render(request, 'edit/album_form.html')
#     return resp

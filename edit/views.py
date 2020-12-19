from django.forms import (
    ModelForm,
    inlineformset_factory,
    modelform_factory,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from music.models import Album, Artist, Credit, Recording, Track


# Create your views here.
class RecordingCreate(CreateView):
    model = Recording
    fields = '__all__'
    template_name = 'edit/recording_form.html'


class RecodingUpdate(UpdateView):
    model = Recording
    fields = '__all__'
    template_name = 'edit/recording_form.html'


class RecordingDelete(DeleteView):
    model = Recording
    success_url = reverse_lazy('music:index')
    fields = '__all__'
    template_name = 'edit/recording_form.html'


class AlbumDelete(DeleteView):
    model = Album
    template_name = 'music/album_form.html'
    success_url = reverse_lazy('music:index')
    fields = '__all__'


class AlbumForm(ModelForm):
    prefix = 'album'

    class Meta:
        model = Album
        fields = '__all__'


TrackUpdateFormSet = inlineformset_factory(
    Album, Track, fields=('track_number', 'recording'), extra=0
)
TrackCreateFormSet = inlineformset_factory(
    Album, Track, fields=('track_number', 'recording'), extra=1, can_delete=False
)


def album_create(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album = album_form.save()
            track_formset = TrackUpdateFormSet(request.POST, instance=album)
            if track_formset.is_valid():
                track_formset.save()
                resp = HttpResponseRedirect(
                    reverse('music:album-detail', kwargs={'pk': album.pk})
                )
            else:
                form = {'album_form': album_form, 'track_formset': track_formset}
                resp = render(request, 'edit/album_form.html', form)
        else:
            track_formset = TrackUpdateFormSet(request.POST)
            form = {'album_form': album_form, 'track_formset': track_formset}
            resp = render(request, 'edit/album_form.html', form)
    else:
        form = {
            'album_form': AlbumForm(),
            'track_formset': TrackCreateFormSet(initial=[{'track_number': 1}]),
        }
        resp = render(request, 'edit/album_form.html', form)
    return resp


def album_update(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        track_formset = TrackUpdateFormSet(request.POST, instance=album)
        if album_form.is_valid() and track_formset.is_valid():
            album_form.save()
            track_formset.save()
            resp = HttpResponseRedirect(
                reverse('music:album-detail', kwargs={'pk': album.pk})
            )
        else:
            form = {'album_form': album_form, 'track_formset': track_formset}
            resp = render(request, 'edit/album_form.html', form)
    else:
        form = {
            'album_form': AlbumForm(instance=album),
            'track_formset': TrackUpdateFormSet(instance=album),
        }
        resp = render(request, 'edit/album_form.html', form)
    return resp

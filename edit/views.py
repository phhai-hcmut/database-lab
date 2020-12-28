from django.forms import (
    ModelForm,
    inlineformset_factory,
    modelform_factory,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from music.models import Album, Artist, Credit, Recording, Track


# Create your views here.
class RecordingCreate(LoginRequiredMixin, CreateView):
    model = Recording
    fields = '__all__'
    template_name = 'edit/recording_form.html'


class RecodingUpdate(LoginRequiredMixin, UpdateView):
    model = Recording
    fields = '__all__'
    template_name = 'edit/recording_form.html'


class RecordingDelete(LoginRequiredMixin, DeleteView):
    model = Recording
    success_url = reverse_lazy('music:index')
    fields = '__all__'
    template_name = 'edit/recording_form.html'


class AlbumDelete(LoginRequiredMixin, DeleteView):
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


class AlbumCreate(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
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
        return resp

    def get(self, request, *args, **kwargs):
        form = {
            'album_form': AlbumForm(),
            'track_formset': TrackCreateFormSet(initial=[{'track_number': 1}]),
        }
        return render(request, 'edit/album_form.html', form)


class AlbumUpdate(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        album = Album.objects.get(pk=pk)
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
        return resp

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        album = Album.objects.get(pk=pk)
        form = {
            'album_form': AlbumForm(instance=album),
            'track_formset': TrackUpdateFormSet(instance=album),
        }
        return render(request, 'edit/album_form.html', form)

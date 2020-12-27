from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import (
    ModelForm,
    inlineformset_factory,
    HiddenInput,
)
from django import forms
from django.urls import reverse, reverse_lazy

from .models import Playlist, PlaylistContent
from music.models import Recording
from listening.models import InQueue


class PlaylistIndex(LoginRequiredMixin, ListView):
    # template_name = 'playlist/user_playlist.html'
    template_name = 'music/list_page/playlist_list.html'
    context_object_name = 'playlist_list'

    def get_queryset(self):
        return self.request.user.playlist_set.order_by('name')


class PlaylistDetail(DetailView):
    template_name = 'music/playlist_detail.html'
    model = Playlist

    def get(self, *args, **kwargs):
        resp = super().get(*args, **kwargs)
        if not self.object.is_public and self.request.user != self.object.user:
            raise PermissionDenied("Sorry, this playlist is private.")
        return resp


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        exclude = ('tracks',)
        widgets = {'user': HiddenInput()}


class PlaylistCreate(LoginRequiredMixin, CreateView):
    model = Playlist
    template_name = 'edit/recording_form.html'
    form_class = PlaylistForm

    def get_initial(self):
        return {'user': self.request.user.pk}


class PlaylistUpdate(UpdateView):
    model = Playlist
    template_name = 'edit/recording_form.html'
    form_class = PlaylistForm


class PlaylistDelete(DeleteView):
    model = Playlist
    template_name = 'edit/recording_form.html'
    success_url = reverse_lazy('playlist:playlist-index')


class UserPlaylistsForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        query = Playlist.objects.filter(user=user)
        self.fields['playlists'] = forms.ModelMultipleChoiceField(
            query, widget=forms.CheckboxSelectMultiple
        )


class PlaylistAddRecording(FormView):
    template_name = 'edit/recording_form.html'
    form_class = UserPlaylistsForm
    success_url = '/'

    def get_form(self, form_class=None):
        if self.request.POST:
            form = self.form_class(self.request.user, self.request.POST)
        else:
            form = self.form_class(self.request.user)
        return form

    def form_valid(self, form):
        print("called.............")
        playlists = form.cleaned_data['playlists']
        recording = Recording.objects.get(pk=self.kwargs['recording_pk'])
        for playlist in playlists:
            PlaylistContent(playlist=playlist, recording=recording).save()
        return super().form_valid(form)

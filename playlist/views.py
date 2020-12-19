from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.forms import (
    ModelForm,
    inlineformset_factory,
    modelform_factory,
    HiddenInput,
)
from django.urls import reverse, reverse_lazy

from .models import Playlist
from listening.models import InQueue


@login_required
def index(request):
    """Render a list of user's playlists"""
    playlist_list = Playlist.objects.filter(user=request.user).order_by('name').all()
    in_queue = InQueue.objects.filter(user=request.user).order_by('queue_index')
    return render(
        request,
        'playlist/user_playlist.html',
        {'playlist_list': playlist_list, 'in_queue': in_queue},
    )


# def playlist_list(request):
#     playlist_list = Playlist.objects.order_by('name').all()
#     in_queue = InQueue.objects.filter(user = request.user).order_by('queue_index')
#     # TODO: link html file
#     return render(request, 'music/list_page/playlist_list.html', {'playlist_list': playlist_list,
#                                                                   'in_queue': in_queue})


def playlist_list(request):
    playlist_list = Playlist.objects.order_by('name').all()
    in_queue = InQueue.objects.filter(user=request.user).order_by('queue_index')
    # TODO: link html file
    return render(
        request,
        'music/list_page/playlist_list.html',
        {'playlist_list': playlist_list, 'in_queue': in_queue},
    )


def detail(request, pk):
    """Render a list of tracks in the playlist"""
    # TODO: link to templates
    playlist = Playlist.objects.get(pk=pk)
    if not playlist.is_public and request.user != playlist.user:
        resp = HttpResponse("Private playlist", status=401)
    else:
        resp = HttpResponse("A list of tracks in the playlist")
    return render(request, 'music/playlist_detail.html', {'playlist': playlist})


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        exclude = ('tracks',)
        widgets = {'user': HiddenInput()}


class UserFormMixin:
    def get_initial(self):
        return {'user': self.request.user.pk}


class PlaylistCreate(UserFormMixin, CreateView):
    model = Playlist
    template_name = 'edit/recording_form.html'
    form_class = PlaylistForm


class PlaylistUpdate(UpdateView):
    model = Playlist
    template_name = 'edit/recording_form.html'
    form_class = PlaylistForm


class PlaylistDelete(DeleteView):
    model = Playlist
    template_name = 'edit/recording_form.html'
    success_url = reverse_lazy('playlist:playlist-index')

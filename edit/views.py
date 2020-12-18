from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.forms import formset_factory, ModelForm

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


class TrackForm(ModelForm):
    class Meta:
        model = Track
        fields = ['track_number', 'recording']


TrackFormSet = formset_factory(TrackForm)


def test_formset(request):
    return render(request, 'music/album_form.html', {'form': TrackFormSet()})

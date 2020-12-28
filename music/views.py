from django.views.generic.base import TemplateView
from playlist.models import Playlist

from .models import Album, Artist, Recording


class HomePageView(TemplateView):
    """Render only top track/artist/album for homepage compact display"""

    TOP_NUMBER = 5
    template_name = 'music/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_album_list'] = Album.objects.all()[: self.TOP_NUMBER]
        context['top_recording_list'] = Recording.objects.all()[: self.TOP_NUMBER]
        context['top_artist_list'] = Artist.objects.all()[: self.TOP_NUMBER]
        context['top_playlist'] = Playlist.objects.visible(self.request.user).order_by(
            '-time_created'
        )[: self.TOP_NUMBER]
        return context

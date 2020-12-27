from django.conf import settings
from django.db import models
from django.urls import reverse

from music.models import Recording


class PlaylistManager(models.Manager):
    def visible(self, user):
        query = models.Q(is_public=True)
        if user.is_authenticated:
            query = query | models.Q(user=user)
        return self.get_queryset().filter(query)


class Playlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    tracks = models.ManyToManyField(Recording, through='PlaylistContent')
    objects = PlaylistManager()

    class Meta:
        unique_together = ['user', 'name']

    def get_absolute_url(self):
        return reverse('playlist:playlist-detail', kwargs={'pk': self.pk})

    @property
    def song_list(self):
        return self.tracks.order_by('playlistcontent')


class PlaylistContent(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('time_added',)

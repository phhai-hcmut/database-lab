from django.conf import settings
from django.db import models

from music.models import Recording


class InQueue(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
    queue_index = models.PositiveIntegerField()

    class Meta:
        unique_together = ['user', 'queue_index']


class UserQueue(models.Model):
    class RepeatState(models.TextChoices):
        NO_REPEAT = 0, 'No Repeat'
        REPEAT_CURRENT = 1, 'Repeat Current Song'
        REPEAT_ALL = 2, 'Repeat All Playlist'

    recording = models.ForeignKey(InQueue, on_delete=models.CASCADE)
    repeat_state = models.CharField(choices=RepeatState.choices, max_length=200)
    is_playing = models.BooleanField()
    progress = models.DurationField()

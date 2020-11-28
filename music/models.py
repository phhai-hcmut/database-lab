from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator


class Artist(models.Model):
    name = models.CharField()


class Album(models.Model):
    name = models.CharField()
    release_date = models.DateField()
    artist = models.ManyToManyField(Artist, on_delete=models.CASCADE)

    AlbumType = models.TextChoices('AlbumType', 'SINGLE EP ALBUM')
    album_type = models.CharField(choices=AlbumType)


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()
    name = models.CharField()
    duration = models.DurationField(validators=[MinValueValidator(timedelta())])
    artist_credits = models.ManyToManyField(Artist, through='Credit')

    class Meta:
        unique_together = ['album', 'track_number']


class Credit(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    CreditRole = models.TextChoices('CreditRole', 'PERFORMER PRODUCER WRITER')
    role = models.CharField(choices=CreditRole)


class User(models.Model):
    online = models.BooleanField()
    display_name = models.CharField(unique=True)


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    tracks = models.ManyToManyField(Track, through='PlaylistContent')

    class Meta:
        unique_together = ['artist', 'name']


class PlaylistContent(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now_add=True)


class QueueTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    queue_index = models.PositiveIntegerField()

    class Meta:
        unique_together = ['user', 'queue_index']


class CurrentlyListening(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    track = models.ForeignKey(QueueTrack, on_delete=models.CASCADE)
    RepeatState = models.TextChoices('RepeatState', 'NO_REPEAT REPEAT_ONE REPEAT_ALL')
    repeat_state = models.CharField(choices=RepeatState)
    is_playing = models.BooleanField()
    progress = models.DurationField()

from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.deletion import CASCADE


class Artist(models.Model):
    name = models.CharField(max_length=200)

class Album(models.Model):
    class AlbumType (models.TextChoices):
        EPS = 1, 'Single Extended Play Album'
        SINGLE  = 2, 'Single Album'
        COMPILATION = 3, 'Compilation Album'
        REMIX = 4, 'Remix Album'

    name = models.CharField(max_length=200)
    release_date = models.DateField()
    artist = models.ManyToManyField(Artist) #NOTE: this does auto cascade so it does not have on_delete attribute.
    album_type = models.CharField(choices=AlbumType.choices,max_length=200)

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    duration = models.DurationField(validators=[MinValueValidator(timedelta())])
    artist_credits = models.ManyToManyField(Artist, through='Credit')

    class Meta:
        unique_together = ['album', 'track_number']


class Credit(models.Model):
    class CreditRole(models.TextChoices):
        PERFORMER= 1, 'Performer'
        DIRECTOR= 2, 'Director'
        PRODUCER= 3, 'Producer'
        WRITER= 4, 'Writer'

    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(choices=CreditRole.choices, max_length=200)

class User(models.Model):
    online = models.BooleanField()
    display_name = models.CharField(unique=True,max_length=200)


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
    tracks = models.ManyToManyField(Track, through='PlaylistContent')

    class Meta:
        unique_together = ['user', 'name']


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
    class RepeatState(models.TextChoices):
        NO_REPEAT = 0, 'No Repeat'
        REPEAT_CURRENT = 1 , 'Repeat Current Song'
        REPEAT_ALL = 2, 'Repeat All Playlist'
    
    user = models.OneToOneField(User,on_delete=CASCADE,primary_key=True)
    track = models.ForeignKey(QueueTrack, on_delete=models.CASCADE)
    repeat_state = models.CharField(choices=RepeatState.choices,max_length=200)
    is_playing = models.BooleanField()
    progress = models.DurationField()

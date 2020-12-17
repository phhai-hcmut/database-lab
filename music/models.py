from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser, Group


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Recording(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DurationField(validators=[MinValueValidator(timedelta())])
    artist_credits = models.ManyToManyField(Artist, through='Credit',related_name='artist_credit')


class Album(models.Model):
    class AlbumType(models.TextChoices):
        SINGLE = 1, 'Single'
        EP = 2, 'Extended Play'
        ALBUM = 3, 'Album'

    name = models.CharField(max_length=200)
    release_date = models.DateField()
    # NOTE: this does auto cascade so it does not have on_delete attribute.
    owner = models.ManyToManyField(Artist, related_name='album')
    album_type = models.CharField(choices=AlbumType.choices, max_length=200)

    def __str__(self) -> str:
        artists = [str(a) for a in self.owner.all()]
        return f"{self.name}, {self.release_date}, {self.album_type}, Artists: {artists}"


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='track')
    track_number = models.PositiveIntegerField()
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE,related_name='track')

    class Meta:
        unique_together = ['album', 'track_number']

    def __str__(self) -> str:
        track_name = self.recording.name
        return f"{self.track_number}. {track_name}, {self.recording.duration}"


class Credit(models.Model):
    class CreditRole(models.TextChoices):
        PERFORMER = 1, 'Performer'
        DIRECTOR = 2, 'Director'
        PRODUCER = 3, 'Producer'
        WRITER = 4, 'Writer'

    recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(choices=CreditRole.choices, max_length=200)
    class Meta:
        unique_together = ['recording', 'artist','role']
    def __str__(self) -> str:
        return f"{self.recording}, {self.artist}, {self.role}"

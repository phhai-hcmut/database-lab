from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    class AlbumType(models.TextChoices):
        EPS = 1, 'Single Extended Play Album'
        SINGLE = 2, 'Single Album'
        COMPILATION = 3, 'Compilation Album'
        REMIX = 4, 'Remix Album'

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
    name = models.CharField(max_length=200)
    duration = models.DurationField(validators=[MinValueValidator(timedelta())])
    artist_credits = models.ManyToManyField(Artist, through='Credit', related_name='artist_credit')

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

    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(choices=CreditRole.choices, max_length=200)

    def __str__(self) -> str:
        return f"{self.recording}, {self.artist}, {self.role}"


class User(AbstractUser):
    class UserRole(models.TextChoices):
        ADMIN = 1, 'Administrator'
        MOD = 2, 'Moderator'
        ARTIST = 3, 'Artist'
        LISTENER = 4, 'Listener (normal user)'

    class Meta:
        unique_together = ['user', 'name']

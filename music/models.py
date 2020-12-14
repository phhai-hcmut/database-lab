from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractBaseUser


class Artist(models.Model):
    name = models.CharField(max_length=200)


class Recording(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DurationField(validators=[MinValueValidator(timedelta())])
    artist_credits = models.ManyToManyField(Artist, through='Credit')


class Album(models.Model):
    class AlbumType(models.TextChoices):
        SINGLE = 1, 'Single'
        EP = 2, 'Extended Play'
        ALBUM = 3, 'Album'

    name = models.CharField(max_length=200)
    release_date = models.DateField()
    artist = models.ManyToManyField(
        Artist
    )  # NOTE: this does auto cascade so it does not have on_delete attribute.
    album_type = models.CharField(choices=AlbumType.choices, max_length=200)


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()
    recording = models.ForeignKey(Recording, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['album', 'track_number']


class Credit(models.Model):
    class CreditRole(models.TextChoices):
        PERFORMER = 1, 'Performer'
        DIRECTOR = 2, 'Director'
        PRODUCER = 3, 'Producer'
        WRITER = 4, 'Writer'

    recording = models.ForeignKey(Recording, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(choices=CreditRole.choices, max_length=200)


class User(AbstractBaseUser):
    class UserRole(models.TextChoices):
        ADMIN = 1, 'Administrator'
        MOD = 2, 'Moderator'
        ARTIST = 3, 'Artist'
        LISTENER = 4, 'Listener (normal user)'

    username = models.CharField(unique=True, max_length=200)
    USERNAME_FIELD = 'username'
    online = models.BooleanField()
    role = models.CharField(choices=UserRole.choices, max_length=200)

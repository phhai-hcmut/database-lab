from datetime import timedelta

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('music:artist-detail', kwargs={'pk': self.pk})

    @property
    def owned_albums(self):
        return self.album.order_by('-release_date')

    @property
    def credits(self):
        return self.credit_set.all()

    class Meta:
        ordering = ('name',)


class Recording(models.Model):
    name = models.CharField(max_length=200)
    duration = models.DurationField(validators=[MinValueValidator(timedelta())])
    artist_credits = models.ManyToManyField(
        Artist, through='Credit', related_name='artist_credit'
    )
    genres = models.ManyToManyField(
        'Genre', related_name='recordings', db_table='recording_genre'
    )

    def get_absolute_url(self):
        return reverse('music:recording-detail', kwargs={'pk': self.pk})

    def get_artist_names(self, sep=","):
        artist_names = list(set(artist.name for artist in self.artist_credits.all()))
        return sep.join(artist_names)

    @property
    def artist_names(self):
        return self.get_artist_names()


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
    genres = models.ManyToManyField(
        'Genre', related_name='albums', db_table='album_genre'
    )

    def __str__(self) -> str:
        artists = [str(a) for a in self.owner.all()]
        return (
            f"{self.name}, {self.release_date}, {self.album_type}, Artists: {artists}"
        )

    def get_absolute_url(self):
        return reverse('album-detail', kwargs={'pk': self.pk})

    @property
    def track_list(self):
        return self.track.order_by('track_number')

    @property
    def owner_list(self):
        return self.owner.distinct()

    class Meta:
        ordering = ('-release_date',)


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='track')
    track_number = models.PositiveIntegerField()
    recording = models.ForeignKey(
        Recording, on_delete=models.CASCADE, related_name='track'
    )

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
        unique_together = ['recording', 'artist', 'role']

    def __str__(self) -> str:
        return f"{self.recording}, {self.artist}, {self.role}"


class Genre(models.Model):
    name = models.TextField()

    @property
    def album_list(self):
        return Album.objects.filter(genres=self)

    @property
    def recording_list(self):
        return Recording.objects.filter(genres=self)

    class Meta:
        db_table = 'genre'

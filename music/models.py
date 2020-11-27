from django.db import models


class CreditRole(SQLiteEnum):
    PERFORMER = 0
    PRODUCER = 1
    WRITER = 2


class RepeatState(SQLiteEnum):
    NO_REPEAT = 0
    REPEAT_ONE = 1
    REPEAT_ALL = 2


class Artist(models.Model):
    name = models.CharField()


class Album(models.Model):
    name = models.CharField()
    release_date = models.DateField()
    # class AlbumType(SQLiteEnum):
    #     SINGLE = 0
    #     EP = 1
    #     ALBUM = 2
    AlbumType = models.TextChoices('AlbumType', 'SINGLE EP ALBUM')

    album_type = models.CharField(choices=AlbumType)


class Track(models.Model):
    album = models.Model(Album, on_delete=models.CASCADE)
    name = models.CharField()
    duration = models.DurationField()


class Playlist(models.Model):
    name = models.CharField()
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField()

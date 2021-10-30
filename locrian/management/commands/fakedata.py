from random import choice, randint

from django.core.management.base import BaseCommand
from django.db import transaction

from music import factories, models

NUM_ARTISTS = 100
NUM_RECORDINGS = 1_000
NUM_ALBUMS = 500
MAX_TRACKS_PER_ALBUM = 5
credit_roles = [x[0] for x in models.Credit.CreditRole.choices]


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # self.stdout.write("Deleting old data...")
        # models = [User, Thread, Comment, Club]
        # for m in models:
        #     m.objects.all().delete()

        self.stdout.write("Creating new data...")
        artists = []
        recordings = []
        albums = []

        for _ in range(NUM_ARTISTS):
            artists.append(factories.ArtistFactory())

        for _ in range(NUM_RECORDINGS):
            recording = factories.RecordingFactory()
            recordings.append(recording)
            for role in range(1, 5):
                models.Credit.objects.create(
                    artist=choice(artists),
                    recording=recording,
                    role=role,
                )

        for _ in range(NUM_ALBUMS):
            album = factories.AlbumFactory()
            for _ in range(3):
                album.owner.add(choice(artists))
            for track_number in range(1, randint(1, MAX_TRACKS_PER_ALBUM) + 1):
                models.Track.objects.create(
                    album=album,
                    track_number=track_number,
                    recording=choice(recordings),
                )

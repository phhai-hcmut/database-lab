from random import choice, randint, randrange

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

import listening
import music
import playlist
from locrian.factories import UserFactory
from music.factories import AlbumFactory, ArtistFactory, RecordingFactory
from playlist.factories import PlaylistFactory

NUM_ARTISTS = 100
NUM_RECORDINGS = 1_000
NUM_ALBUMS = 500
MAX_TRACKS_PER_ALBUM = 5
NUM_USERS = 100
NUM_PLAYLISTS = 500
MAX_RECORDINGS_PER_PLAYLIST = 10
MAX_RECORDINGS_PER_QUEUE = 10

credit_roles = [x[0] for x in music.models.Credit.CreditRole.choices]


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = Faker()
        # self.stdout.write("Deleting old data...")
        # models = [User, Thread, Comment, Club]
        # for m in models:
        #     m.objects.all().delete()

        self.stdout.write("Creating new data...")
        artists = []
        recordings = []
        albums = []
        users = []

        for _ in range(NUM_ARTISTS):
            artists.append(ArtistFactory())

        for _ in range(NUM_RECORDINGS):
            recording = RecordingFactory()
            recordings.append(recording)
            for role in range(1, 5):
                music.models.Credit.objects.create(
                    artist=choice(artists),
                    recording=recording,
                    role=role,
                )

        for _ in range(NUM_ALBUMS):
            album = AlbumFactory()
            for _ in range(3):
                album.owner.add(choice(artists))
            for track_number in range(1, randint(1, MAX_TRACKS_PER_ALBUM) + 1):
                music.models.Track.objects.create(
                    album=album,
                    track_number=track_number,
                    recording=choice(recordings),
                )

        for _ in range(NUM_USERS):
            users.append(UserFactory())

        for _ in range(NUM_PLAYLISTS):
            playlist_obj = PlaylistFactory(user=choice(users))
            for _ in range(MAX_RECORDINGS_PER_PLAYLIST):
                playlist.models.PlaylistContent.objects.create(
                    playlist=playlist_obj,
                    recording=choice(recordings),
                )

        for user in users:
            queue_length = randint(1, MAX_RECORDINGS_PER_QUEUE)
            user_queue = [
                listening.models.InQueue.objects.create(
                    user=user,
                    recording=choice(recordings),
                    queue_index=i,
                )
                for i in range(queue_length)
            ]
            listening_song = choice(user_queue)
            listening.models.UserQueue.objects.create(
                user=user,
                recording=listening_song,
                progress=fake.time_delta(
                    end_datetime=listening_song.recording.duration
                ),
                repeat_state=randrange(3),
                is_playing=choice([False, True]),
            )

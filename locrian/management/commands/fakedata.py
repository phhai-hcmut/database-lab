from itertools import product
from random import choice, randint, randrange

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from faker.providers.person.en import Provider

import listening
import music
import playlist
from locrian.factories import UserFactory
from music.factories import AlbumFactory, ArtistFactory, RecordingFactory
from playlist.factories import PlaylistFactory

NUM_ARTISTS = 30_000
NUM_RECORDINGS = 300_000
NUM_ALBUMS = 150_000
MAX_TRACKS_PER_ALBUM = 5
NUM_USERS = 50_000
NUM_PLAYLISTS = 150_000
MAX_RECORDINGS_PER_PLAYLIST = 50
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
        genres = [
            music.models.Genre.objects.create(name='Pop'),
            music.models.Genre.objects.create(name='Rock'),
            music.models.Genre.objects.create(name='Country'),
            music.models.Genre.objects.create(name='Blue'),
        ]

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
            album.genres.add(*fake.random_sample(genres))
            album_artists = fake.random_sample(artists, length=randint(1, 3))
            album.owner.add(*album_artists)
            album_tracks = fake.random_sample(
                recordings, length=randint(1, MAX_TRACKS_PER_ALBUM)
            )
            for i, recording in enumerate(album_tracks):
                music.models.Track.objects.create(
                    album=album,
                    track_number=i + 1,
                    recording=recording,
                )

        unique_names = set(
            map(' '.join, product(Provider.first_names, Provider.last_names))
        )
        random_names = fake.random_sample(
            unique_names, length=min(len(unique_names), NUM_USERS)
        )
        for username in random_names:
            users.append(UserFactory(username=username))

        playlist_names = set(fake.texts(nb_texts=NUM_PLAYLISTS, max_nb_chars=20))
        for playlist_name in playlist_names:
            playlist_obj = PlaylistFactory(name=playlist_name, user=choice(users))
            playlist_recordings = fake.random_sample(
                recordings, length=randint(1, MAX_RECORDINGS_PER_PLAYLIST)
            )
            for recording in playlist_recordings:
                playlist.models.PlaylistContent.objects.create(
                    playlist=playlist_obj,
                    recording=recording,
                    time_added=fake.past_datetime(
                        start_date=playlist_obj.time_created,
                    ),
                )

        for user in users:
            queue_songs = fake.random_sample(
                recordings, length=randint(1, MAX_RECORDINGS_PER_QUEUE)
            )
            user_queue = [
                listening.models.InQueue.objects.create(
                    user=user,
                    recording=recording,
                    queue_index=i,
                )
                for i, recording in enumerate(queue_songs)
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

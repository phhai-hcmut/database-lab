from random import randint
from datetime import timedelta

import factory
from factory.django import DjangoModelFactory

from . import models


class ArtistFactory(DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = models.Artist


class AlbumFactory(DjangoModelFactory):
    name = factory.Faker('text', max_nb_chars=20)
    release_date = factory.Faker('date_object')
    album_type = 3

    class Meta:
        model = models.Album


class RecordingFactory(DjangoModelFactory):
    name = factory.Faker('text', max_nb_chars=20)
    duration = factory.Faker('time_delta', end_datetime=timedelta(minutes=5))

    class Meta:
        model = models.Recording


class CreditFactory(DjangoModelFactory):
    recording = factory.SubFactory(RecordingFactory)
    artist = factory.SubFactory(ArtistFactory)
    role = factory.Faker(
        'random_element', elements=[x[0] for x in models.Credit.CreditRole.choices]
    )

    class Meta:
        model = models.Credit


class FullRecordingFactory(RecordingFactory):
    artist_credits = factory.RelatedFactory(
        CreditFactory, factory_related_name='recording'
    )


class TrackFactory(DjangoModelFactory):
    album = factory.SubFactory(AlbumFactory)
    track_number = factory.Sequence(lambda n: n)
    recording = factory.SubFactory(RecordingFactory)

    class Meta:
        model = models.Track


class FullAlbumFactory(AlbumFactory):
    @factory.post_generation
    def track(self, create, extracted, **kwargs):
        if not create:
            # Simple build, or nothing to add, do nothing.
            return

        for track_number in range(1, randint(1, 9) + 1):
            TrackFactory(album=self, track_number=track_number)

        for _ in range(randint(1, 5)):
            self.owner.add(ArtistFactory())

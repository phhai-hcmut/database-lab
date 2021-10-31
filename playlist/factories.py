import factory
from factory.django import DjangoModelFactory

from locrian.factories import UserFactory

from . import models


class PlaylistFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    name = factory.Faker('text', max_nb_chars=20)
    description = factory.Faker('text', max_nb_chars=100)
    is_public = factory.Faker('random_element', elements=[True, False])
    time_created = factory.Faker('past_datetime')

    class Meta:
        model = models.Playlist

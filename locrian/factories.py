import factory
from django.conf import settings
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    username = factory.Faker('name')
    password = factory.Faker('password')

    class Meta:
        model = settings.AUTH_USER_MODEL

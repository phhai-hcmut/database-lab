from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.

# class User(AbstractUser):
#     GROUP_TYPES = ['moderator','artist','listener']
#     #online is is_active in AbstractUser
#     username = models.CharField(unique=True, max_length=200)
#     USERNAME_FIELD = 'username'
#     groups = models.ManyToManyField(Group)
from django.contrib import admin
from django.contrib.auth.models import Group

from . import models

admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.Track)
admin.site.register(models.Recording)
admin.site.register(models.Credit)


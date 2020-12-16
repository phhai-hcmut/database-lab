from django.contrib import admin

from .models import InQueue, UserQueue


admin.site.register(InQueue)
admin.site.register(UserQueue)

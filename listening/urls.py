from django.urls import path

from . import views

app_name = 'queue'
urlpatterns = [
    path('', views.list_queue, name='queue-index'),
    path('add/', views.add_song_to_queue, name='queue-song'),
]


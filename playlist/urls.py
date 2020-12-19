from django.urls import path

from . import views
from music.views import playlist_list

app_name = 'playlist'
urlpatterns = [
    path('', playlist_list, name='playlist-index'),
    path('<int:pk>/', views.detail, name='playlist-detail'),
]

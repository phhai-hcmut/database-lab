from django.conf.urls import include
import playlist
from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:pk>/', views.album_detail, name='album-detail'),
    path('artist/<int:pk>/', views.artist_detail, name='artist-detail'),
    path('playlist/', include(('playlist.urls','playlist'), namespace='playlist')),
]

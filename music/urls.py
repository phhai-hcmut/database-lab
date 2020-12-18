from django.conf.urls import include
from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:pk>/', views.album_detail, name='album-detail'),
    path('artist/<int:pk>/', views.artist_detail, name='artist-detail'),
    path('track/<int:pk>', views.track_detail, name='track-detail'),
    path('album/', views.album_list, name='album_list'),
    path('track/', views.track_list, name='track_list'),
    path('artist/', views.artist_list, name='artist_list'),
    path('add/', views.addMusic, name='add'),
]

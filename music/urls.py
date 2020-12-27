from django.conf.urls import include
from django.urls import path
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Album, Artist, Credit, Recording, Track
from .views import HomePageView

app_name = 'music'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('album/<int:pk>/', DetailView.as_view(model=Album), name='album-detail'),
    path('artist/<int:pk>/', DetailView.as_view(model=Artist), name='artist-detail'),
    # path('track/<int:pk>', views.track_detail, name='track-detail'),
    path(
        'recording/<int:pk>/',
        DetailView.as_view(model=Recording),
        name='recording-detail',
    ),
    path(
        'album/',
        ListView.as_view(model=Album, template_name='music/list_page/album_list.html'),
        name='album_list',
    ),
    path(
        'artist/',
        ListView.as_view(
            model=Artist, template_name='music/list_page/artist_list.html'
        ),
        name='artist_list',
    ),
]

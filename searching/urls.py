from django.urls import path

from . import views

urlpatterns = [
    path('search_result/', views.SearchResultView.as_view(), name='search-results'),
    path(
        'search_result/playlist/<str:query>/',
        views.SearchPlaylistView.as_view(),
        name='search-playlist',
    ),
    path(
        'search_result/recording/<str:query>/',
        views.SearchRecordingView.as_view(),
        name='search-recording',
    ),
    path(
        'search_result/artist/<str:query>/',
        views.SearchArtistView.as_view(),
        name='search-artist',
    ),
    path(
        'search_result/album/<str:query>/',
        views.SearchAlbumView.as_view(),
        name='search-album',
    ),
]

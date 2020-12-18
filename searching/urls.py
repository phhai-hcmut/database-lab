 

from django.urls import path

from . import views

urlpatterns = [
    path('search_result/', views.SearchResultView.as_view(), name='search-results'),
    path('search_result/playlist/<str:query>/',views.searchPlaylist, name='search-playlist'),
    path('search_result/track/<str:query>/',views.searchTrack, name='search-track'),
    path('search_result/artist/<str:query>/',views.searchArtist, name='search-artist'),
    path('search_result/album/<str:query>/',views.searchAlbum, name='search-album'),
]

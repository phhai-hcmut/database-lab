from django.urls import path

from . import views

app_name = 'playlist'
urlpatterns = [
    path('', views.PlaylistIndex.as_view(), name='playlist-index'),
    path('<int:pk>/', views.PlaylistDetail.as_view(), name='playlist-detail'),
    path('add/', views.PlaylistCreate.as_view(), name='playlist-add'),
    path('<int:pk>/edit/', views.PlaylistUpdate.as_view(), name='playlist-update'),
    path('<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlist-update'),
    path('add-recording/<int:recording_pk>/', views.PlaylistAddRecording.as_view(), name='playlist-add-recording'),
]

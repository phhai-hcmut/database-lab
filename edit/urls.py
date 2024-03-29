from django.conf.urls import include
from django.urls import path
from . import views

app_name = 'edit'
urlpatterns = [
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    path('album/<int:pk>/edit/', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
    path('recording/add/', views.RecordingCreate.as_view(), name='recording-add'),
    path('recording/<int:pk>/edit/', views.RecodingUpdate.as_view(), name='recording-update'),
    path('recording/<int:pk>/delete/', views.RecordingDelete.as_view(), name='recording-delete'),
]

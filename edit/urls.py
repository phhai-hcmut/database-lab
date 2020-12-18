from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('album/add/', views.test_formset, name='album-add'),
    path('album/<int:pk>/edit/', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]

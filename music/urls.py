from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:pk>/', views.album_detail, name='album-detail'),
]

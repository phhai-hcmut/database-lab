from django.urls import path

from . import views
app_name = 'playlist'
urlpatterns = [
    path('', views.index, name='playlist-index'),
    path('<int:pk>/', views.detail, name='playlist-detail'),
]

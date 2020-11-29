from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='playlist-index'),
    path('<int:pk>/', views.detail, name='playlist-detail'),
]

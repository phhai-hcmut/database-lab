from django.urls import path

from . import views
app_name = 'music'
urlpatterns = [
    # ex: /music/
    #this one list all albums
    path('', views.index, name='index'),
    # ex: /music/5/
    #this one shows one album details
    path('<int:album_id>/', views.detail, name='detail'),
]

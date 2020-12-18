from django.urls import path
from . import views

from music import views as music_view
app_name = 'account'
urlpatterns = [
    # path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # path('listener/', music_view.index, name="listener-page"),
    # path('artist/', music_view.index, name="artist-page"),
]

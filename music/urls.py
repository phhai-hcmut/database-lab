from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
    # path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    # path('', views.index, name='index'),
    path('listener/', views.listenerPage, name="listener-page"),
    path('artist/', views.artistPage, name="artist-page"),
]

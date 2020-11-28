from django.urls import path
from . import views
from user import views as user_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', user_view.login_view, name='login'),
    # path('news/', views.newsPage, name='news'),
    # path('play/', views.playPage, name='play'),
    # path('profile/', views.profilePage, name='profile'),
]
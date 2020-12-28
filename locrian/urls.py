"""locrian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    # NOTE: add the /<your_destination> in the web's url to visit the correct site
    # Example: "http://127.0.0.1:8000/music/" to visit music
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='edit/recording_form.html',
            success_url=reverse_lazy('music:index'),
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page=reverse_lazy('music:index')),
        name='logout',
    ),
    path('', include('account.urls', namespace='account')),
    path('', include('music.urls', namespace='music')),
    path('', include('edit.urls')),
    path('playlist/', include('playlist.urls', namespace='playlist')),
    path('searching/', include(('searching.urls', 'searching'), namespace='searching')),
    # overwire admin logout link
    # path('admin/logout/', lambda request: redirect('account:logout', permanent=False)),
    path('admin/', admin.site.urls, name='admin'),
    path('queue/', include('listening.urls', namespace='queue')),
]

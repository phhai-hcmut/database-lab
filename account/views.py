from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from dataclasses import dataclass
from django.http import HttpResponse

# Create your views here.
# ____________________________AUTHENTICATION VIEWS AND HOME PAGES__________________________

from .decorators import unauthenticated_user,user_redirection,allowed_users


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account:home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('account:login')


@login_required(login_url='account:login')
@user_redirection
def home(request):
    context = {}
    return render(request, 'account/moderator_home.html', context)


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['listener'])
def listenerPage(request):
    context = {}
    return render(request, 'account/listener_home.html', context)


@login_required(login_url='account:login')
@allowed_users(allowed_roles=['artist'])
def artistPage(request):
    context = {}
    return render(request, 'account/artist_home.html', context)
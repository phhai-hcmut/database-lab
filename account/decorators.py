from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import Group, User

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect('account:home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator

def user_redirection(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'listener':
			return redirect('music/')
			# return redirect('account:listener-page')
		
		if group == 'artist':
			return redirect('music/')
			# return redirect('account:artist-page')

		if group == 'moderator':
			return view_func(request, *args, **kwargs)
		
		if request.user.is_superuser:
			return redirect('admin:login')
		print('not a type')
	return wrapper_function
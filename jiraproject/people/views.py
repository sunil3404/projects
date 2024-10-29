from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
	authenticate, 
	login as auth_login,
	logout
	)


# Create your views here.
def registerUser(request):
	user_form = RegisterUserForm()
	if request.method == 'POST':
		user_form = RegisterUserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return redirect('login-user')
		else:
			print("In else", user_form.cleaned_data)
			user_form = RegisterUserForm()
	return render(request, 'people/register.html', {'user_form' : user_form})


def loginUser(request):
	if request.method == 'POST':
		user =  authenticate(request, username=request.POST['username'],
							 password=request.POST['password'])
		if user is not None:
			auth_login(request, user)
			return redirect('user-jiras')
		else:
			print('User not found')
	context = {
		'user_form' : LoginUserForm()
	}
	return render(request, 'people/login.html', context)


@login_required
def logoutUser(request):
	logout(request)
	return redirect("jira-home")

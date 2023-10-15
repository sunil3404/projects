from django.shortcuts import render, redirect
from todoapp import settings
from django.contrib.auth.forms import UserCreationForm
from user.forms import RegisterUserForms, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# print(settings.BASE_DIR)
# print(settings.STATIC_URL)


def loginUser(request):
	if request.user.is_authenticated:
		return redirect("user-tasks")
	form = LoginForm()
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		form = LoginForm(request.POST)
		user = authenticate(username = username, password = password)
		if user:
			if form.is_valid():
				login(request, user)
				messages.add_message(request, messages.SUCCESS, f'Welcome {username}')
				return redirect("user-tasks")
		else:
			messages.add_message(request, messages.WARNING, f'User {username} does not exist!!!')
			print(f"User with { username } not found")
	context = {
		"form" : form
	}
	
	return render(request, "user/login.html" , context)


def registerUser(request):
	form = RegisterUserForms()
	if request.method == 'POST':
		form = RegisterUserForms(request.POST)
		if form.is_valid():
			form.save()
	context = {
		"form" : form
	}
	return render(request, "user/register.html", context)

def logoutUser(request):
	context  = {
		"form" : LoginForm()
	}

	logout(request)
	return render(request, "user/logout.html", context)
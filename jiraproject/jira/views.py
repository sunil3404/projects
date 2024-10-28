from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import IssueForm, RegisterUserForm, LoginUserForm
from .models import JiraIssue
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
	authenticate, 
	login as auth_login,
	logout
	)


# Create your views here.

def jira_home(request):

	context = {

		'issues' : JiraIssue.objects.all()
	}
	return render(request, 'home.html', context)

def create_jira(request):
	form = IssueForm()
	context = {
		'form' : form
	}

	if request.method == 'POST':
		form = IssueForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('jira-home')
		else:
			form  = IssueForm()
	return render(request, 'create_jira.html', context)

@login_required
def updateJira(request, pk):
	obj = get_object_or_404(User, id=1)
	jira = JiraIssue.objects.get(id=pk)
	if request.method == 'POST':
		update_form = IssueForm(request.POST, instance=jira)
		if update_form.is_valid():
			update_form.save()
			return redirect('jira-home')
	
	update_form  = IssueForm(instance=jira)
	context = {

		'update_form' : update_form
	}
	return render(request, 'update_jira.html', context)

def registerUser(request):
	user_form = UserCreationForm()
	if request.method == 'POST':
		user_form = UserCreationForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return redirect('login-user')
		else:
			print("In else", user_form.cleaned_data)
			user_form = UserCreationForm()
	return render(request, 'register.html', {'user_form' : user_form})


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
	return render(request, 'login.html', context)

@login_required
def userJiras(request):
	issues = JiraIssue.objects.filter(assigned_to=request.user)
	context = {
		'issues' : issues
	}
	return render(request, 'user_jiras.html', context)

@login_required
def logoutUser(request):
	logout(request)
	return redirect("jira-home")


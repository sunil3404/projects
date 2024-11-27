from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import IssueForm
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
	return render(request, 'jira/home.html', context)

def create_jira(request):
	form = IssueForm()
	context = {
		'form' : form
	}

	if request.method == 'POST':
		form = IssueForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('show-issues')
		else:
			form  = IssueForm()
	return render(request, 'jira/create_jira.html', context)

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
	return render(request, 'jira/update_jira.html', context)

@login_required
def showIssues(request):
	issues = JiraIssue.objects.filter(assigned_to=request.user)
	context = {
		'issues' : issues
	}
	return render(request, 'jira/issues.html', context)

@login_required
def showIssueDetail(request, pk):
	issue = JiraIssue.objects.filter(id=pk)
	context = {
		'issue' : issue
	}
	return render(request, 'jira/issue_details.html', context)

@login_required
def logoutUser(request):
	logout(request)
	return redirect("jira-home")


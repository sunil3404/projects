from django.shortcuts import render
from .forms import JiraProjectForm
from .models import JiraProject
from jira.models import JiraIssue

# Create your views here.


def create_project(request):
    form = JiraProjectForm()
    if request.method == 'POST':
        form = JiraProjectForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            form = JiraProjectForm()
    context = {
        'form' : form
    }
    return render(request, 'projects/project_create.html', context)

def display_project(request):
    projects = JiraProject.objects.all()
    context = {
        'projects' : projects
    }

    return render(request, 'projects/projects.html', context)

def projectDetail(request, id):
    project  = JiraProject.objects.filter(id = id).first()
    issues = JiraIssue.objects.filter(project_name=id)

    print(issues)
    context = {
        'project' : project,
        'issues'  : issues
    }
    return render(request, 'projects/project_details.html', context)

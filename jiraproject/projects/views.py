from django.shortcuts import render
from .forms import JiraProjectForm
from .models import JiraProject

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
    return render(request, 'projects/project_details.html', {'project' : project})

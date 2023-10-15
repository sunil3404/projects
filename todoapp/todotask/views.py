from django.shortcuts import render, redirect
from todotask.forms import TaskCreateForm, UpdateTaskForm
from todotask.models import UserTasks
from status.models import TaskStatus
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def taskListView(request):
	form = TaskCreateForm()
	if request.method == 'POST':
		form = TaskCreateForm(request.POST, None)
		if form.is_valid():
			tasks_name = form.cleaned_data['task']
			user = User.objects.filter(id=request.user.id).first()
			task = UserTasks(task_name = tasks_name, user_id=user)
			task.save()
			form = TaskCreateForm()
			messages.add_message(request, messages.SUCCESS, f'Successfully Created Task - {tasks_name}')
			return redirect("user-tasks")
	pg = Paginator(UserTasks.objects.filter(user_id=request.user.id), 6)
	tasks = UserTasks.objects.filter(user_id=request.user.id)
	context = {
		"form" : form,
		# "tasks" : UserTasks.objects.filter(user_id=request.user.id),
		"page_obj" : pg.page(request.GET.get('page', 1)),
		"pg_num" : pg.page_range
	}
	return render(request, "todotask/task.html", context)

def updateTaskView(request, task_pk):
	task = UserTasks.objects.filter(id=task_pk).first()
	form = UpdateTaskForm(initial = {"task" : task.task_name, "status" : task.status_id.status.lower()})
	if request.method == "POST":
		form = UpdateTaskForm(request.POST)
		if form.is_valid():
			status = TaskStatus.objects.filter(status__iexact=form.cleaned_data['status']).first()
			utask = UserTasks.objects.filter(id=task_pk).first()
			utask.task_name = form.cleaned_data['task']
			utask.status_id_id = status
			utask.save()
			messages.add_message(request, messages.WARNING, f'Successfully Updated Task - {utask.task_name}')
			return redirect("user-tasks")
	context = {
		"form" : form,
		"task_name" : task.task_name[0:25] + " ..."
	}
	return render(request, "todotask/update.html", context)

def deleteTaskView(request, task_pk):
	task = UserTasks.objects.filter(id=task_pk).first()
	if request.GET.get("id"):
		UserTasks.objects.filter(id = request.GET.get("id")).delete()
		messages.add_message(request, messages.INFO, f'Successfully Deleted Task - {task.task_name}')
		return redirect('user-tasks')
	
	return render(request, "todotask/delete.html", {"task" : task})

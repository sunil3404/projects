from django.urls import path
from todotask import views

urlpatterns = [

	path("tasks/", views.taskListView, name="user-tasks"),
	path("update/<int:task_pk>/", views.updateTaskView, name="usertask-update"),
	path("delete/<int:task_pk>/", views.deleteTaskView, name="usertask-delete"),
]
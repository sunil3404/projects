from django.db import models
from status.models import TaskStatus
from django.contrib.auth.models import User

# Create your models here.

class UserTasks(models.Model):
	task_name = models.CharField(max_length=255)
	task_create_date = models.DateTimeField(auto_now_add=True)
	task_update_date = models.DateTimeField(auto_now=True)

	user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	status_id = models.ForeignKey(TaskStatus, default=1, null=True, on_delete=models.SET_NULL)


	class Meta:
		ordering = ['-task_update_date']
		
	def __str__(self):
		return self.task_name

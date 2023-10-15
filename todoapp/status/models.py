from django.db import models

# Create your models here.

class TaskStatus(models.Model):
	status = models.CharField(max_length=100)


	def __str__(self):
		return self.status

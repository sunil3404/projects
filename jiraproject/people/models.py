from django.db import models

# Create your models here.

class RegisterUser(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.TextField()
	confirm_password = models.TextField()

	def __str__(self):
		return self.username


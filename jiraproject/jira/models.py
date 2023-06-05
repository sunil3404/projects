from django.db import models
from django.contrib.auth.models import User


status = (
	('new', 'NEW'),
	('inprogress', 'INPROGRESS'),
	('complete', 'COMPLETE'),
)

def get_user_id():
	return User.objects.get(id=1)

class JiraIssue(models.Model):
	name = models.CharField(max_length=250)
	detail = models.TextField()
	status = models.CharField(max_length = 50, choices=status, default="new")
	assigned_to=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-date_updated']

	def __str__(self):
		return self.name


class RegisterUser(models.Model):
	username = models.CharField(max_length=100)
	email = models.EmailField()
	password = models.TextField()
	confirm_password = models.TextField()

	def __str__(self):
		return self.username


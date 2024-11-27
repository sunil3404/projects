from django.db import models
from django.contrib.auth.models import User
from projects.models import JiraProject


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
	reported_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='issue_reported_by')
	assigned_to = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='issue_assigned_to')
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	project_name = models.ForeignKey(JiraProject, null=True, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-date_updated']

	def __str__(self):
		return self.name




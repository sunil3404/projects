from django.db import models
from django.contrib.auth import get_user_model

User= get_user_model()


CHOICES = [('BUG', 'bug'), ('ENHANCEMENT', 'enhancement')]
STATUS_CHOICES = [('NEW', 'new'), ('DONE', 'done'), ('INPROGRESS', 'inprogress')]

class IssueType(models.Model):
    story = models.CharField(max_length=20, default='BUG')

    def __str__(self):
        return self.story

class Status(models.Model):
    status = models.CharField(max_length=20, default='NEW')
    def __str__(self):
        return self.status



class Issue(models.Model):
    summary = models.TextField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    assigned_to = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    issue_type = models.ForeignKey(IssueType, blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.summary

class Comment(models.Model):
    post = models.TextField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(Issue, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.post

    
from django.contrib import admin
from .models import Issue, IssueType, Status, Comment
#  JiraUser

# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueType)
admin.site.register(Status)
admin.site.register(Comment)
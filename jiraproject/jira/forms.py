from django import forms
from .models import JiraIssue

# class IssueForm(forms.Form):
	
# 	# name = form.CharField(max_length=100, )
# 	name = forms.CharField(label="Issue Title",max_length=100)
# 	detail = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Description')
# 	status = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}), label="Jira Status")

class IssueForm(forms.ModelForm):
	
	# name = form.CharField(max_length=100, )
	class Meta:
		model = JiraIssue
		fields = ('name', 'detail', 'status', 'assigned_to', 'project_name')
		# choices = ['New', 'InProgress', 'InReview', 'Done']
		ordered = ['-date_created']

		labels = {
			'name' : 'Title',
			'detail' : 'Description',
			'project_name' : 'Project'

		}
		widgets = {

			'name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'detail' : forms.Textarea(attrs={'class' : 'form-control'}),
			'status' : forms.Select(attrs={'class' : 'form-control'}),
			'assigned_to' : forms.Select(attrs={'class' : 'form-control'}),
			'project_name' : forms.Select(attrs={'class' : 'form-control'}),
		}


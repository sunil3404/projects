from django.forms import ModelForm
from django import forms
from .models import JiraProject



class JiraProjectForm(ModelForm):


	class Meta:
		model = JiraProject
		fields = ('name', 'description')

		labels = {
			'name' : 'Project Name',
			'description' : 'Project Description'
		}

		widgets = {
				'Project Name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter ProjectName'}),
				'Project Description' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Project Description'})
		}
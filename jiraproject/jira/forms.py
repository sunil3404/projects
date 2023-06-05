from django import forms
from .models import JiraIssue, RegisterUser

# class IssueForm(forms.Form):
	
# 	# name = form.CharField(max_length=100, )
# 	name = forms.CharField(label="Issue Title",max_length=100)
# 	detail = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label='Description')
# 	status = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}), label="Jira Status")

class IssueForm(forms.ModelForm):
	
	# name = form.CharField(max_length=100, )
	class Meta:
		model = JiraIssue
		fields = ('name', 'detail', 'status', 'assigned_to')
		# choices = ['New', 'InProgress', 'InReview', 'Done']
		ordered = ['-date_created']

		labels = {
			'name' : 'Title',
			'detail' : 'Description'

		}
		widgets = {

			'name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'detail' : forms.Textarea(attrs={'class' : 'form-control row-2'}),
			'status' : forms.Select(attrs={'class' : 'form-control col-4'}),
			'assigned_to' : forms.Select(attrs={'class' : 'form-control col-4'})
		}

class RegisterUserForm(forms.ModelForm):

	class Meta:
		model = RegisterUser
		fields = ('username', 'email', 'password', 'confirm_password')


		labels = {
			'username' : 'Username',
			'email'    : 'Email',
			'password' : 'Password',
			'confirm_password' : 'Confirm Password'

		}

		widgets = {

				'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Usename'}),
				'email' : forms.TextInput(attrs={'class' : 'form-control'}),
				'password' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'password'}),
				'confirm_password' : forms.TextInput(attrs={'class' : 'form-control', 'type':'password'})
		}

class LoginUserForm(forms.ModelForm):

	class Meta:
		model = RegisterUser
		fields = ('username', 'password')

		labels = {
			'username'    : '',
			'password' : '',

		}

		widgets = {
				'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Enter User Username"}),
				'password' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'password', 'placeholder' : 'Enter Password'})
		}
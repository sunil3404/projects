from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class RegisterUserForms(UserCreationForm):

	email 			= forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class" : "form-control"}))
	first_name 		= forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class" : "form-control"}))
	last_name 		= forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class" : "form-control"}))

	class Meta():
		model = User
		fields = (
				  "email", 
				  "first_name", 
				  "last_name", 
				  "username", 
				  "password1", 
				  "password2"
				  )
		widgets = { 
			'username'  : forms.TextInput(attrs={'class'     : 'form-control'}),
			'password1' : forms.PasswordInput(attrs={'class' : 'form-control'}),
			'password2' : forms.PasswordInput(attrs={'class' : 'form-control'}),
     	}


class LoginForm(forms.Form):
	username       = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class" : "form-control"}))
	password       = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class" : "form-control"}))




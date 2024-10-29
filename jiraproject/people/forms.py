from django import forms
from .models import RegisterUser


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
			'username'    : 'Username',
			'password' : 'Password',

		}

		widgets = {
				'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Enter User Username"}),
				'password' : forms.TextInput(attrs={'class' : 'form-control', 'type': 'password', 'placeholder' : 'Enter Password'})
		}
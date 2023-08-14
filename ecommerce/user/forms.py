from django import forms
from django.core.exceptions import ValidationError
#product_name = forms.CharField(label="Product Name", 
#            widget=forms.TextInput(attrs={"class" : "form-control"}), max_length=100)

class LoginForm(forms.Form):
    
    email = forms.EmailField(label="",
            widget=forms.EmailInput(attrs={"class" : "form-control", "placeholder" : "Email"}))
    password = forms.CharField(label="",
            widget=forms.PasswordInput(attrs={"class" : "form-control", "type" : "password", "placeholder" : "Password"}))

class RegisterForm(forms.Form):

    username = forms.CharField(label="", 
            widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Username" }))
    email = forms.EmailField(label="", 
            widget=forms.EmailInput(attrs={"class" : "form-control", "placeholder" : "Enter Email"}))
    address = forms.CharField(label="",
            widget=forms.Textarea(attrs={"class" : "form-control", "placeholder" : "Address" }))
    password = forms.CharField(label="", 
            widget=forms.PasswordInput(attrs={"class" : "form-control", "type" : "password", "placeholder" : "Password" }))
    password1 = forms.CharField(label="", 
            widget=forms.PasswordInput(attrs={"class" : "form-control", "type" : "password", "placeholder" : "Confirm Password" }))

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password1")

        if  password != confirm_password:
            msg = "Password Mismatch"
            self.add_error("password1", msg)
        return self.cleaned_data

class AddressForm(forms.Form):
    username = forms.CharField(label="", 
            widget=forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Username" }))
    email = forms.EmailField(label="", 
            widget=forms.EmailInput(attrs={"class" : "form-control", "placeholder" : "Enter Email"}))
    address = forms.CharField(label="",
            widget=forms.Textarea(attrs={"class" : "form-control", "placeholder" : "Address" }))


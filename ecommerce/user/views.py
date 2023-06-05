from django.shortcuts import render, redirect
from user.forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from user.models import MyUser

# Create your views here.


def loginUser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = MyUser.objects.filter(email=request.POST['email']).first()
        if user and form.is_valid():
            login(request, user)
            return redirect('product-home')
    return render(request, "user/login.html", {"form" : form })

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data.pop("password1")
            MyUser.objects.create(**form.cleaned_data)
            return redirect("user-login")
    return render(request, "user/register.html", {"form" : form })

def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html')

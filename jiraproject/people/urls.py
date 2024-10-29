from django.urls import path
from . import views

urlpatterns =[
	path("register/", views.registerUser, name='register-user'),
	path("login_user/", views.loginUser, name='login-user'),
	path("logout_user/", views.logoutUser, name="logout-user"),
]
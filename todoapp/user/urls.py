from django.urls import path
from user.views import (loginUser, registerUser)

urlpatterns = [
	path("login/", loginUser, name="user-login" ),
	path("register/", registerUser, name="user-register")
]
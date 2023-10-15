from django.urls import path
from user.views import (loginUser, registerUser, logoutUser)

urlpatterns = [
	path("login/", loginUser, name="user-login" ),
	path("register/", registerUser, name="user-register"),
	path("logout/", logoutUser, name="user-logout")
]
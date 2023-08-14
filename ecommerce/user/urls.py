from django.urls import path
from user import views


urlpatterns = [
    path("login/", views.loginUser, name="user-login"),
    path("register/", views.registerUser, name="user-register"),
    path("logout/", views.logout_user, name="user-logout"),
    #path("orderSummary/", views.addNewAddress, name="user-add"),


]


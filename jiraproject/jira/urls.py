from django.urls import path
from . import views

urlpatterns =[

	path("", views.jira_home, name='jira-home'),
	path("create_jira/", views.create_jira, name='create-issue'),
	path("update_jira/<pk>", views.updateJira, name='update-jira'),
	path("logout_user/", views.logoutUser, name="logout-user"),
	path("user_jiras/", views.userJiras, name='user-jiras'),
]
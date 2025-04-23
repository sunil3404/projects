from django.urls import path
from . import views

urlpatterns = [
    path('', views.jira_home, name='home'),
    path('jira/<int:pk>', views.get_issue, name='display-issue'),
    path('jira/create', views.create_issue, name='create-issue'),
    path('jira/<int:pk>/delete', views.delete_issue, name='delete-issue'),
    path('jira/<int:pk>/update', views.update_issue, name='update-issue'),

    #Comment URLS
    path('jira/comments/<int:id>', views.get_comments, name='comments'),
    path('jira/comment/add', views.create_comment, name='create-comment'),

    #STORY URLS
    path('jira/story', views.get_stories, name='story'),

    #STATUS URLS
    path('jira/status', views.get_status, name='status'),

    #User
    path('jira/users', views.get_users, name='users'),
    path('jira/register', views.register_user, name='register-user')
]

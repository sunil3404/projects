from django.urls import path
from . import views

urlpatterns =[
	path("create_project/", views.create_project, name='create-project'),
    path("projects/", views.display_project, name='show-projects'),
    path("project/<int:id>/detail", views.projectDetail, name='show-details'),
]
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render, redirect


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('jira.urls')),
    path("", include('people.urls'))
]

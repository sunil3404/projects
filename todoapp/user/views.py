from django.shortcuts import render
from todoapp import settings
from django.contrib.auth.forms import UserCreationForm

print(settings.BASE_DIR)
print(settings.STATIC_URL)


def loginUser(request):
	return render(request, "user/login.html" , {})


def registerUser(request):
	form = UserCreationForm()
	context = {
		"form" : form
	}
	return render(request, "user/register.html", context)
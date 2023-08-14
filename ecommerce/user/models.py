from django.db import models
from django.contrib.auth.models import AbstractUser


CR = "CUSTOMER"
ad = "ADMIN"

ROLES  = [
    (CR, "CUSTOMER"),
    (ad, "ADMIN")
]

class MyUser(AbstractUser):
    role=models.CharField(max_length=100, choices=ROLES)
    email = models.EmailField(max_length=250, unique=True)
    address = models.CharField(max_length=20000, blank=True, null=True)

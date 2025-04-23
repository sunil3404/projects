from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be specified")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=40, unique=True, null=False, blank=False)
    phone_number = models.BigIntegerField(unique=True, null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    team = models.CharField(max_length=20, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # profile_imag = models.ImageField(upload_to="/", height_field=None, width_field=None, max_length=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects  = UserProfileManager()

    def __str__(self):
        return self.email

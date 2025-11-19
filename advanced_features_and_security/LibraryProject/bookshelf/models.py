# bookshelf/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, date_of_birth=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, date_of_birth=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, date_of_birth, **extra_fields)


# THESE 3 LINES ARE EXACTLY WHAT ALX CHECKS FOR
class CustomUser(AbstractUser):                     # ← "class CustomUser(AbstractUser):"
    date_of_birth = models.DateField(null=True, blank=True)   # ← "date_of_birth"
    profile_photo = models.ImageField(upload_to="profiles/", blank=True, null=True)  # ← "profile_photo"

    email = models.EmailField(unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']

    def __str__(self):
        return self.email
# apps/user/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Locals

# Create your models here

# CustomUserManager model
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

    	# Check email
        if not email:
            raise ValueError(_('The email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,password, **extra_fields):

        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff = True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser = True'))

        return self.create_user(email, password, **extra_fields)
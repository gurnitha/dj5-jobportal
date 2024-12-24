# apps/users/admin.py

# Django modules
from django.contrib import admin

# My modules
from users.models import CustomUser

# Register your models here.

admin.site.register(CustomUser)


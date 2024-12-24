# apps/users/urls.py

# Django modules
from django.urls import path

# My modules
from users import views

# namespace
app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
]

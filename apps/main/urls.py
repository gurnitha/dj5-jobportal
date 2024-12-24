# apps/main/urls.py

# Django modules
from django.urls import path

# My modules
from main import views

# namespace
app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
]

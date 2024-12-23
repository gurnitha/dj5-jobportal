# apps/jobs/urls.py

# Django modules
from django.urls import path

# My modules
from jobs import views

# namespace
app_name = 'jobs'

urlpatterns = [
    path('', views.home_view, name='home'),
]

# apps/jobs/urls.py

# Django modules
from django.urls import path

# My modules
from jobs import views

# namespace
app_name = 'jobs'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('job/lists/', views.jobs_list_view, name='jobs_list'),
    path('job/create/', views.job_create_view, name='job_create'),
]

# apps/jobs/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home_view(request):
	return render(request, 'jobs/index.html')


def jobs_list_view(request):
	return render(request, 'jobs/jobs_list.html')


def job_create_view(request):
	return render(request, 'jobs/job_create.html')
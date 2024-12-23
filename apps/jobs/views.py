# apps/jobs/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home_view(request):
	return render(request, 'jobs/index.html')
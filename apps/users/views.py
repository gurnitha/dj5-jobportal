# apps/users/views.py

# Django modules
from django.shortcuts import render

# Create your views here.


def register_view(request):
	return render(request, 'users/register.html')
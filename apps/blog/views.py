# apps/blog/views.py

# Django modules
from django.shortcuts import render

# Create your views here.


def posts_list_view(request):
	return render(request, 'blog/posts_list.html')
# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # users
    path('', include('users.urls', namespace='users')),
    # jobs
    path('', include('jobs.urls', namespace='jobs')),
    # main
    path('', include('main.urls', namespace='main')), 
    # blog
    path('', include('blog.urls', namespace='blog')), 
    path('admin/', admin.site.urls),
]

# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # jobs
    path('', include('jobs.urls', namespace='jobs')), 
    # blog
    path('', include('blog.urls', namespace='blog')), 
    path('admin/', admin.site.urls),
]

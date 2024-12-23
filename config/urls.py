# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # jobs
    path('', include('jobs.urls', namespace='jobs')), 
    path('admin/', admin.site.urls),
]

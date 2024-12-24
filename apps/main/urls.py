# apps/main/urls.py

# Django modules
from django.urls import path

# My modules
from main import views

# namespace
app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]

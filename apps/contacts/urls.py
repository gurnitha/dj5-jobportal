# apps/contacts/urls.py

# Django modules
from django.urls import path

# My modules
from contacts import views

# namespace
app_name = 'contacts'

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
]

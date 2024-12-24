# apps/contacts/views.py

# Django modules
from django.shortcuts import render

# Create your views here.


def contact_view(request):
	return render(request, 'contacts/contact.html')


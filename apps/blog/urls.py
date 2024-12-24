# apps/blog/urls.py

# Django modules
from django.urls import path

# My modules
from blog import views

# namespace
app_name = 'blog'

urlpatterns = [
    path('blog/', views.posts_list_view, name='posts_list'),
]

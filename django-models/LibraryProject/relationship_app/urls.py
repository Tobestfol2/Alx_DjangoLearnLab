# relationship_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Task 1: Views & URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Task 2: Authentication using Django's built-in class-based views
    path('register/', views.register_view, name='register'),

    # REQUIRED LINES: LoginView & LogoutView with template_name
    path('login/', 
         auth_views.LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'),
    
    path('logout/', 
         auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'),
]
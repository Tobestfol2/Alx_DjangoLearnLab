# relationship_app/urls.py
from django.urls import path
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

app_name = 'relationship_app'

urlpatterns = [
    # Existing URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Role-Based Views
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
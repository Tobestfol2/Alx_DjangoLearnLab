# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library   # REQUIRED LINE


# FUNCTION-BASED VIEW: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# CLASS-BASED VIEW: Detail view of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
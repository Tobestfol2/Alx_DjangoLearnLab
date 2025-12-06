# api/views.py
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# Task 1 – Keep this for /books/ (List only)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Step 1: Create BookViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model with all CRUD operations:
    - list: GET /books_all/
    - retrieve: GET /books_all/<id>/
    - create: POST /books_all/
    - update: PUT /books_all/<id>/
    - destroy: DELETE /books_all/<id>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
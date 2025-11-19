# bookshelf/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Book

@login_required
def search_books(request):
    query = request.GET.get('q', '')
    if query:
        # SAFE: Uses Django ORM (no raw SQL)
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/search.html', {'books': books, 'query': query})
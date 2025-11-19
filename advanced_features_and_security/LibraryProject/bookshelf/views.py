# bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from .models import Book


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        Book.objects.create(title=title, author=author, added_by=request.user)
        messages.success(request, "Book created!")
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'action': 'Create'})


@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        messages.success(request, "Book updated!")
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'action': 'Edit', 'book': book})


@login_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted!")
        return redirect('book_list')
    return render(request, {'book': book})
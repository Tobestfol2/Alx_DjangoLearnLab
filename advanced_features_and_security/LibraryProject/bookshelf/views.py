# bookshelf/views.py
# bookshelf/views.py
from .forms import ExampleForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Book
from .forms import ExampleForm   # THIS LINE IS REQUIRED BY ALX
from .forms import BookForm   # Now imports correctly

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})
# relationship_app/librarian_view.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_librarian(user):
    return user.profile.role == 'Librarian'


@user_passes_test(is_librarian, login_url='relationship_app:login')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
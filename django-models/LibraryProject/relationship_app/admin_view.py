# relationship_app/admin_view.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_admin(user):
    return user.profile.role == 'Admin'


@user_passes_test(is_admin, login_url='relationship_app:login')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
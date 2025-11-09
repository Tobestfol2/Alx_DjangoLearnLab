# relationship_app/member_view.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


def is_member(user):
    return user.profile.role == 'Member'


@user_passes_test(is_member, login_url='relationship_app:login')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
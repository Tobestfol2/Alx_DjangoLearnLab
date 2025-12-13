from django.urls import path
from . import views

urlpatterns = [
    # Your existing blog URLs (post list, detail, etc.) go here...

    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.profile_view, name='profile'),
]
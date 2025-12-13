from django.urls import path, include   # make sure 'include' is imported
# ... your existing urlpatterns from the first task ...

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),  # adds login, logout, password change, etc.
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
]
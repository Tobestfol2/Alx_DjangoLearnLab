# bookshelf/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Custom Admin for CustomUser
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_of_birth', 'is_staff')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)


# REQUIRED BY ALX CHECKER – THIS LINE MUST BE PRESENT
admin.site.register(CustomUser, CustomUserAdmin)
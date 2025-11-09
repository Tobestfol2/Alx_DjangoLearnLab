from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # 1. Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # 2. Enable search by title and author
    search_fields = ('title', 'author')

    # 3. Add filters on the right sidebar
    list_filter = ('publication_year', 'author')

    # Optional: Order by publication year (newest first)
    ordering = ('-publication_year',)
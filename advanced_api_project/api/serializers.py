# api/serializers.py
from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.
    Includes custom validation to prevent future publication years.
    """
    
    class Meta:
        model = Book
        fields = '__all__'  # title, publication_year, author, id

    def validate_publication_year(self, value):
        """
        Custom validation: Book cannot be published in the future
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year: {current_year}"
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author with nested Book data.
    Uses BookSerializer (many=True) to include all related books.
    """
    books = BookSerializer(many=True, read_only=True)  # NESTED SERIALIZER

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
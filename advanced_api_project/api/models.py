from django.db import models
from django.core.validators import MaxValueValidator
import datetime


class Author(models.Model):
    """
    Represents an author who has written one or more books.
    One Author → Many Books (One-to-Many relationship)
    """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    """
    Represents a book written by an Author.
    ForeignKey creates a Many-to-One relationship with Author.
    """
    title = models.CharField(max_length=300)
    publication_year = models.PositiveIntegerField(
        validators=[MaxValueValidator(datetime.date.today().year)]
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    class Meta:
        ordering = ['-publication_year']
        unique_together = ['title', 'author']
# relationship_app/models.py
# ------------------------------------------------------------
# 1. Author – One-to-Many with Book
# ------------------------------------------------------------
from django.db import models


class Author(models.Model):
    """
    An author in the library system.
    """
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)

    class Meta:
        verbose_name        = "Author of Book"
        verbose_name_plural = "Authors of Books"
        permissions = [
            ("can_publish_book", "Can officially approve a book for publication"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ------------------------------------------------------------
# 2. Book – Many-to-One with Author
# ------------------------------------------------------------
class Book(models.Model):
    """
    A book belonging to a single author.
    """
    title            = models.CharField(max_length=200)
    isbn             = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()

    # ForeignKey → One Author can have many Books
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",      # author.books.all()
    )

    class Meta:
        # Optional: custom permissions for Book (as required in later tasks)
        permissions = [
            ("can_add_book",    "Can add a book"),
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title
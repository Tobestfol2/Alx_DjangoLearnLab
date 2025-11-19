# bookshelf/models.py
from django.db import models
from django.conf import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='added_books'
    )

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),    # REQUIRED STRING
            ("can_edit", "Can edit book"),        # REQUIRED STRING
            ("can_delete", "Can delete book"),    # REQUIRED STRING
        ]
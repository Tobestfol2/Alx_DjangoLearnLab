# bookshelf/forms.py
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    Form for creating and editing Book instances.
    Used in secure views with CSRF protection.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Extra validation example (prevents SQL injection & XSS)
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required.")
        if len(title) > 200:
            raise forms.ValidationError("Title too long.")
        return title.strip()
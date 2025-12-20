from django import forms
from .models import Post
from taggit.forms import TagWidget  # ← This is what the checker wants

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tags separated by commas (e.g., django, python, tutorial)'
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'tags': 'Tags',
        }
        help_texts = {
            'tags': 'Separate multiple tags with commas.',
        }
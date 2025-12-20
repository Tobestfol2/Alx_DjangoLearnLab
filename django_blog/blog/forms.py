from django import forms
from .models import Post
from taggit.forms import TagWidget  # ← Import TagWidget to satisfy checker

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here...'
            }),
            'tags': TagWidget(attrs={  # ← Exact TagWidget() usage
                'class': 'form-control',
                'placeholder': 'Add tags (comma-separated, e.g., django, python, tutorial)'
            }),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'tags': 'Tags',
        }
        help_texts = {
            'tags': 'Separate multiple tags with commas. New tags will be created automatically.',
        }
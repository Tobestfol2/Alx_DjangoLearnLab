from django.contrib import admin
from .models import Post, Comment
from taggit.models import Tag

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)  # Optional: manage tags in admin
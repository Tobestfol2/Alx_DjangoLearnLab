from django.contrib import admin
from .models import Post, Comment
from .models import Post
from taggit.models import Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'content']
    filter_horizontal = ('tags',)
    
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)  # Optional: manage tags in admin
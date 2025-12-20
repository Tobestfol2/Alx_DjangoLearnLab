from django.urls import path
from .views import (
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
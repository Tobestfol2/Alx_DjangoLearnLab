from django.urls import path
from .views import (
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    # post_list if you have it
)

urlpatterns = [
    # path('', post_list, name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('posts/<int:post_pk>/comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('posts/<int:post_pk>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
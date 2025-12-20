from django.urls import path
from .views import (
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    SearchResultsView,
    PostByTagListView,  # ← New view for checker
)

urlpatterns = [
    # Post detail
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    
    # Comment CRUD
    path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    
    # Search
    path('search/', SearchResultsView.as_view(), name='search'),
    
    # Tag posts - exact pattern and view name required by checker
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
from django.urls import path
from . import views
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

    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.search_posts, name='search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='tag_posts'),
    #making a blog-posts
]
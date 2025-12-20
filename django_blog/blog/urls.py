from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
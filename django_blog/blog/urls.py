urlpatterns += [
    path('post/', PostListView.as_view(), name='post_list'),                 
    path('post/new/', PostCreateView.as_view(), name='post_create'),            
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),       
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet


# Step 2: Set up DefaultRouter and register BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # REQUIRED BY ALX

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]
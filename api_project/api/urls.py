from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token   # REQUIRED BY ALX
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Task 1 & Task2
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),

    # Task 3: Token login endpoint
    path('auth/login/', obtain_auth_token, name='api_token_auth'),  # POST username + password → get token
]
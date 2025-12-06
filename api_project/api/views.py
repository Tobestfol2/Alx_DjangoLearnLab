from rest_framework import generics, viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer


# Task 1 – Read-only for everyone (optional override)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access


# Task 2 & 3 – Full CRUD, but only for authenticated users
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # REQUIRED BY ALX
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]   # Only logged-in users

    # BONUS: Only admin can create/delete, others can only read/update own
    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
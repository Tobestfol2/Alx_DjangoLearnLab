from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.admin = User.objects.create_superuser(username='admin', password='admin123')

        # Create sample books
        self.book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        self.book2 = Book.objects.create(title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960)

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', kwargs={'pk': pk})
        self.delete_url = lambda pk: reverse('book-delete', kwargs={'pk': pk})

        # Clients
        self.client = APIClient()

    # 1. Test List Books - Anyone can view
    def test_list_books_unauthenticated(self):
        response = self.client.get(self.list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # 2. Test Retrieve Single Book - Anyone can view
    def test_retrieve_book_unauthenticated(self):
        response = self.client.get(self.detail_url(self.book1.pk))
        serializer = BookSerializer(self.book1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    # 3. Test Create Book - Only authenticated users
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "publication_year": 1925
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest('id').title, "The Great Gatsby")

    def test_create_book_unauthenticated(self):
        data = {"title": "Should Fail", "author": "Anonymous", "publication_year": 2023}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 4. Test Update Book - Only authenticated users
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        data = {"title": "Updated Title", "author": "New Author", "publication_year": 2000}
        response = self.client.put(self.update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        response = self.client.put(self.update_url(self.book1.pk), {"title": "Hack"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 5. Test Delete Book - Only authenticated users
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.delete(self.delete_url(self.book2.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 6. Bonus: Test Filtering, Searching, Ordering (if you added them)
    def test_search_by_title(self):
        response = self.client.get(self.list_url, {'search': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_ordering_by_year(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
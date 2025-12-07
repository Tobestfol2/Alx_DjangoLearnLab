from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from ..models import Book
from ..serializers import BookSerializer


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a normal user and a superuser
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass123')

        # Create sample books
        self.book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        self.book2 = Book.objects.create(title="Animal Farm", author="George Orwell", publication_year=1945)
        self.book3 = Book.objects.create(title="Brave New World", author="Aldous Huxley", publication_year=1932)

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

        # Client
        self.client = APIClient()

    # 1. List books — anyone can view
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    # 2. Retrieve single book — anyone can view
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    # 3. Create book — only authenticated
    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"title": "New Book", "author": "New Author", "publication_year": 2025}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        data = {"title": "Hack", "author": "Hacker", "publication_year": 9999}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 4. Update book — only authenticated
    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {"title": "Updated 1984"}
        response = self.client.patch(self.detail_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated 1984")

    def test_update_book_unauthenticated(self):
        response = self.client.patch(self.detail_url(self.book1.pk), {"title": "Hack"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 5. Delete book — only authenticated
    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url(self.book2.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # 6. Filtering
    def test_filter_by_author(self):
        response = self.client.get(self.list_url, {'author': 'George Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # 7. Searching
    def test_search_by_title(self):
        response = self.client.get(self.list_url, {'search': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # 8. Ordering
    def test_ordering_by_year_desc(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, [1949, 1945, 1932])
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters


class BookAPITests(APITestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username='user', password='pass123')
        self.superuser = User.objects.create_superuser(username='admin', password='admin123')

        # Create sample books
        self.book1 = Book.objects.create(title="Django for Beginners", author="William Vincent", publication_year=2020)
        self.book2 = Book.objects.create(title="Python Crash Course", author="Eric Matthes", publication_year=2019)

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

        # Client
        self.client = APIClient()

    def test_list_books_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_unauthenticated(self):
        response = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Django for Beginners")

    def test_create_book_authenticated(self):
        self.client.login(username='user', password='pass123')
        data = {"title": "New Book", "author": "New Author", "publication_year": 2025}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertTrue(Book.objects.filter(title="New Book").exists())

    def test_create_book_unauthenticated(self):
        data = {"title": "Hack", "author": "Hacker", "publication_year": 9999}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username='user', password='pass123')
        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_update_book_unauthenticated(self):
        response = self.client.patch(self.detail_url(self.book1.pk), {"title": "Hack"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        self.client.login(username='user', password='pass123')
        response = self.client.delete(self.detail_url(self.book2.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filtering(self):
        response = self.client.get(self.list_url, {'author': 'William Vincent'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search(self):
        response = self.client.get(self.list_url, {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [item['publication_year'] for item in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
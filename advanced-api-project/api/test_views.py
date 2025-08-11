"""
Unit tests for Book API endpoints.

Covers:
- CRUD operations (create, list, retrieve, update, delete)
- Permissions: create/update/delete require authentication
- Validation: publication_year cannot be in the future
- Filtering, searching, ordering on the list endpoint

Run:
    python manage.py test api
"""

from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model

from .models import Author, Book

User = get_user_model()


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Ensure using DRF's APIClient, not Django's Client
        from rest_framework.test import APIClient
        self.client = APIClient()

        # Create a user for authenticated actions
        self.user = User.objects.create_user(username='tester', password='password123')

        # Create an author and some books
        self.author = Author.objects.create(name="Test Author")
        self.book1 = Book.objects.create(title="Alpha", publication_year=2010, author=self.author)
        self.book2 = Book.objects.create(title="Beta", publication_year=2015, author=self.author)
        self.book3 = Book.objects.create(title="Gamma Magic", publication_year=2020, author=self.author)

        # Base endpoints (adjust if your project's URL prefix differs)
        self.list_url = '/api/books/'
        self.create_url = '/api/books/create/'
        # update/delete endpoints use pk
        self.detail_url = lambda pk: f'/api/books/{pk}/'
        self.update_url = lambda pk: f'/api/books/{pk}/update/'
        self.delete_url = lambda pk: f'/api/books/{pk}/delete/'

    # Helper to authenticate client
    def auth(self):
        # Ensure self.client is DRF's APIClient
        from rest_framework.test import APIClient
        if not isinstance(self.client, APIClient):
            self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    # --- List / filtering / search / ordering ---

    def test_list_books_returns_all(self):
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # expect at least the three created books
        self.assertGreaterEqual(len(resp.json()), 3)

    def test_filter_by_publication_year(self):
        resp = self.client.get(self.list_url, {'publication_year': 2015})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Only book2 has 2015
        data = resp.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Beta')

    def test_search_title_and_author_name(self):
        # search by part of title
        resp = self.client.get(self.list_url, {'search': 'Magic'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Gamma' in b['title'] for b in resp.json()))

        # search by author name
        resp2 = self.client.get(self.list_url, {'search': 'Test Author'})
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        # All books belong to Test Author -> results should include them
        self.assertGreaterEqual(len(resp2.json()), 3)

    def test_ordering_by_publication_year_desc(self):
        resp = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        years = [b['publication_year'] for b in data]
        # Should be non-increasing
        self.assertTrue(all(years[i] >= years[i+1] for i in range(len(years)-1)))

    # --- Retrieve single book ---

    def test_retrieve_book(self):
        resp = self.client.get(self.detail_url(self.book1.pk))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        self.assertEqual(data['title'], self.book1.title)
        self.assertEqual(data['publication_year'], self.book1.publication_year)

    # --- Create ---

    def test_create_book_unauthenticated_forbidden(self):
        payload = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.pk
        }
        resp = self.client.post(self.create_url, payload, format='json')
        # expecting 401 Unauthorized (since IsAuthenticated required)
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_create_book_authenticated_success(self):
        self.auth()
        payload = {
            'title': 'New Book Auth',
            'publication_year': 2019,
            'author': self.author.pk
        }
        resp = self.client.post(self.create_url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # Check DB
        exists = Book.objects.filter(title='New Book Auth').exists()
        self.assertTrue(exists)

    def test_create_book_future_publication_year_rejected(self):
        self.auth()
        next_year = timezone.now().year + 1
        payload = {
            'title': 'Future Book',
            'publication_year': next_year,
            'author': self.author.pk
        }
        resp = self.client.post(self.create_url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', resp.json())

    # --- Update ---

    def test_update_book_unauthenticated_forbidden(self):
        payload = {'title': 'Alpha Updated', 'publication_year': 2010, 'author': self.author.pk}
        resp = self.client.put(self.update_url(self.book1.pk), payload, format='json')
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_update_book_authenticated_success(self):
        self.auth()
        payload = {'title': 'Alpha Updated', 'publication_year': 2011, 'author': self.author.pk}
        resp = self.client.put(self.update_url(self.book1.pk), payload, format='json')
        # UpdateAPIView should return 200 on success
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Alpha Updated')
        self.assertEqual(self.book1.publication_year, 2011)

    def test_update_with_future_year_rejected(self):
        self.auth()
        future = timezone.now().year + 2
        payload = {'title': 'Alpha', 'publication_year': future, 'author': self.author.pk}
        resp = self.client.put(self.update_url(self.book1.pk), payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', resp.json())

    # --- Delete ---

    def test_delete_book_unauthenticated_forbidden(self):
        resp = self.client.delete(self.delete_url(self.book2.pk))
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_delete_book_authenticated_success(self):
        self.auth()
        resp = self.client.delete(self.delete_url(self.book2.pk))
        # DestroyAPIView returns 204 on success
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())


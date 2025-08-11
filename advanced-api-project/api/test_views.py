from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # Log in the test user
        self.client.login(username="testuser", password="testpassword")

        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_year=2024
        )

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_create_book(self):
        data = {
            "title": "Another Book",
            "author": "Jane Doe",
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "Another Book")

    def test_update_book(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ✅ Verify update reflected in data
        self.assertEqual(response.data['title'], "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # ✅ Ensure deletion
        self.assertFalse(Book.objects.filter(pk=self.book.id).exists())

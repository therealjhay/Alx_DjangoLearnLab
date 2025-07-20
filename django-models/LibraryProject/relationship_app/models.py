# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

class Author(models.Model):
    """
    A model to represent an author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    A model to represent a book.
    - ForeignKey to Author for the one-to-many relationship.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Library(models.Model):
    """
    A model to represent a library.
    - ManyToManyField to Book for the many-to-many relationship.
    """
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    """
    A model to represent a librarian.
    - OneToOneField to Library for the one-to-one relationship.
    """
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# New: UserProfile Model for Role-Based Access Control
class UserProfile(models.Model):
    """
    Extends Django's User model to include a role for role-based access control.
    """
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"
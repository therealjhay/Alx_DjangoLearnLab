from django.db import models
from django.utils import timezone

class Author(models.Model):
    """
    Represents an author.
    One author can have multiple books (One-to-Many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book.
    Each book is linked to exactly one author via ForeignKey.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

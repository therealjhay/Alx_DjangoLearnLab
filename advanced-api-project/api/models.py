from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# The Author model is a simple representation of a book's author.
# It has a single field, 'name', to store the author's full name.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# The Book model represents a single book.
# It has a title, a publication year, and a foreign key to the Author model.
# The 'related_name' attribute on the ForeignKey allows us to easily access
# the books from an Author instance (e.g., author.books.all()).
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f'"{self.title}" by {self.author.name}'

    def clean(self):
        """Custom model validation to ensure publication year is not in the future."""
        current_year = timezone.now().year
        if self.publication_year > current_year:
            raise ValidationError("Publication year cannot be in the future.")

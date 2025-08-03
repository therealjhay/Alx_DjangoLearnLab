from django.db import models

# Create your models here.

class Book(models.Model):
    """
    Represents a book in the library.

    Attributes:
        title (CharField): The title of the book, with a maximum length of 200 characters.
        author (CharField): The author of the book, with a maximum length of 100 characters.
        publication_year (IntegerField): The year the book was published.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of the Book instance.
        This is useful for displaying the object in the Django admin and shell.
        """
        return f"{self.title} by {self.author} ({self.publication_year})"

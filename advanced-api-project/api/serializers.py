from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

# The BookSerializer handles serialization for the Book model.
# It serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation for the publication_year field.
    # This method is automatically called by DRF's validation process.
    def validate_publication_year(self, value):
        """
        Check that the publication year is not in the future.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# The AuthorSerializer serializes the Author model.
# It uses a nested BookSerializer to display all books associated with an author.
# The 'books' field matches the 'related_name' in the Book model's ForeignKey.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
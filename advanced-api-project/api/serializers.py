from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model, validating that the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model, including a nested list of the author's books.
    """
    books = BookSerializer(many=True, read_only=True)  # related_name='books' in the model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

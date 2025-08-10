from rest_framework import generics, permissions, serializers
from .models import Book
from .serializers import BookSerializer
from django.utils import timezone
"from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated"

# 📄 ListView — Retrieve all books (public)
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to anyone (no authentication required).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# 📄 DetailView — Retrieve a single book by ID (public)
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details for a single book by its ID.
    Accessible to anyone (no authentication required).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✏ CreateView — Add a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to add a new book.
    Validates that publication year is not in the future.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Extra validation logic
        year = serializer.validated_data.get('publication_year')
        if year > timezone.now().year:
            raise serializers.ValidationError(
                {"publication_year": "Year cannot be in the future."}
            )
        serializer.save()


# 🔄 UpdateView — Modify an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Extra validation logic
        year = serializer.validated_data.get('publication_year')
        if year > timezone.now().year:
            raise serializers.ValidationError(
                {"publication_year": "Year cannot be in the future."}
            )
        serializer.save()


# ❌ DeleteView — Remove a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

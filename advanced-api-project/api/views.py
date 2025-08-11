from rest_framework import generics, filters as drf_filters
from django_filters import rest_framework as filters
from .models import Book
from rest_framework import generics, permissions, serializers
from django.utils import timezone
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter
    ]

    # Step 1: Filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Step 2: Searching
    search_fields = ['title', 'author']

    # Step 3: Ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering

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

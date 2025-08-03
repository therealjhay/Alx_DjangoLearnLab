from rest_framework import generics, viewsets # <-- Make sure 'viewsets' is imported here
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Existing BookList view (you can keep it for now, or remove it if not needed separately)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New BookViewSet for full CRUD operations
class BookViewSet(viewsets.ModelViewSet): # This line now has 'viewsets' defined
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
from django.urls import path, include
from rest_framework.routers import DefaultRouter # Import DefaultRouter
from .views import BookList, BookViewSet # Make sure to import BookViewSet

# Create a router instance
router = DefaultRouter()
# Register your BookViewSet with the router
# The 'r' before the string denotes a raw string, good practice for regex
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView) - keep if you still want this specific list-only endpoint
    # path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    # The router automatically generates URLs like /books_all/, /books_all/{id}/
    path('', include(router.urls)),
]
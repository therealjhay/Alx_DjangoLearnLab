from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# 📘 Function-based view: List all books
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 🏛️ Class-based view: Show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # Used in template as {{ library }}

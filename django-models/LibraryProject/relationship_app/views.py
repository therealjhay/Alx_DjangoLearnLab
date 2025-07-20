# LibraryProject/relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from . models import Book, Library  # This line imports the necessary models

# Function-based view to list all books
def list_books(request):
    """
    Renders a list of all books and their authors.
    """
    books = Book.objects.all().select_related('author')
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays the details of a single library, including its books.
    This view expects a primary key (pk) in the URL.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

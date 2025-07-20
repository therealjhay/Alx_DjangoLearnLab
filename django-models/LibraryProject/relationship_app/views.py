# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Book, Library

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

# Function-based view for user registration
def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

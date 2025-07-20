# relationship_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm # For registration
from django.contrib.auth import login # For automatic login after registration
from django.contrib.auth.views import LoginView, LogoutView # Built-in views

from .models import Book, Library

# Function-based view to list all books (from previous task)
def list_books(request):
    """
    Renders a list of all books and their authors.
    """
    books = Book.objects.all().select_related('author')
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library (from previous task)
class LibraryDetailView(DetailView):
    """
    Displays the details of a single library, including its books.
    This view expects a primary key (pk) in the URL.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# New: Function-based view for user registration
def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after registration
            return redirect('books_list') # Redirect to books list or a dashboard
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# New: Class-based view for user login
class CustomLoginView(LoginView):
    """
    Handles user login using Django's built-in LoginView.
    """
    template_name = 'relationship_app/login.html'
    # success_url is configured via LOGIN_REDIRECT_URL in settings.py

# New: Class-based view for user logout
class CustomLogoutView(LogoutView):
    """
    Handles user logout using Django's built-in LogoutView.
    """
    template_name = 'relationship_app/logout.html'
    # next_page is configured via LOGOUT_REDIRECT_URL in settings.py
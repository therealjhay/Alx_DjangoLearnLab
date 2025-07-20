# relationship_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test # New imports

from .models import Book, Library, UserProfile # Updated import

# Helper functions for role checking
def is_admin(user):
    """Checks if the user has the 'Admin' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Checks if the user has the 'Librarian' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Checks if the user has the 'Member' role."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

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

# Function-based view for user registration (from previous task)
def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # UserProfile is created automatically by signal
            login(request, user)
            return redirect('books_list')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# New: Role-based views
@login_required # Ensures user is logged in
@user_passes_test(is_admin, login_url='/app/login/') # Redirects to login if not admin
def admin_view(request):
    """
    View accessible only to Admin users.
    """
    return render(request, 'relationship_app/admin_view.html', {'message': 'Welcome, Admin!'})

@login_required
@user_passes_test(is_librarian, login_url='/app/login/')
def librarian_view(request):
    """
    View accessible only to Librarian users.
    """
    return render(request, 'relationship_app/librarian_view.html', {'message': 'Welcome, Librarian!'})

@login_required
@user_passes_test(is_member, login_url='/app/login/')
def member_view(request):
    """
    View accessible only to Member users.
    """
    return render(request, 'relationship_app/member_view.html', {'message': 'Welcome, Member!'})
# advanced_features_and_security/bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.forms import ModelForm
from .models import Book

# Simple Book Form for demonstration
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'published_date']

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Displays a list of all books. Requires 'can_view' permission.
    """
    books = Book.objects.all()
    # Pass permission checks to the template to conditionally show buttons
    user_can_create = request.user.has_perm('bookshelf.can_create')
    user_can_edit = request.user.has_perm('bookshelf.can_edit')
    user_can_delete = request.user.has_perm('bookshelf.can_delete')

    context = {
        'books': books,
        'user_can_create': user_can_create,
        'user_can_edit': user_can_edit,
        'user_can_delete': user_can_delete,
    }
    return render(request, 'bookshelf/book_list.html', context)

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    Allows creation of a new book. Requires 'can_create' permission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user # Assign the current user as the adder
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Add'})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    Allows editing an existing book. Requires 'can_edit' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    Allows deleting a book. Requires 'can_delete' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# Basic Login View (if you don't have one, for testing)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('book_list') # Redirect to book list after login
    else:
        form = AuthenticationForm()
    return render(request, 'bookshelf/login.html', {'form': form})


# advanced_features_and_security/bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
# from django.http import HttpResponseForbidden, HttpResponse # Not strictly needed for this task
from django.forms import ModelForm
from .models import Book
# For search example if implemented
from django.db.models import Q # For complex queries, preventing injection

# Example of a secure search view (assuming you add a search input to book_list.html)
# This demonstrates safe handling of user input for queries.
# Add this function to your views.py
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_search(request):
    """
    Handles secure searching of books using Django ORM's Q objects.
    Prevents SQL injection by not using raw string formatting for queries.
    """
    query = request.GET.get('q') # Get the search query from GET parameters
    books = Book.objects.all()

    if query:
        # Use Q objects for complex lookups (OR conditions)
        # Django's ORM automatically handles SQL injection prevention here.
        books = books.filter(
            Q(title__icontains=query) |
            Q(author_name__icontains=query)
        )

    user_can_create = request.user.has_perm('bookshelf.can_create')
    user_can_edit = request.user.has_perm('bookshelf.can_edit')
    user_can_delete = request.user.has_perm('bookshelf.can_delete')

    context = {
        'books': books,
        'query': query, # Pass query back to template for display
        'user_can_create': user_can_create,
        'user_can_edit': user_can_edit,
        'user_can_delete': user_can_delete,
    }
    return render(request, 'bookshelf/book_list.html', context) # Render the same list template

# ... (rest of your existing views like book_list, book_create, book_edit, book_delete, login_view) ...

# Original book_list view (if you want to keep it separate from search):
# @login_required
# @permission_required('bookshelf.can_view', raise_exception=True)
# def book_list(request):
#     books = Book.objects.all()
#     user_can_create = request.user.has_perm('bookshelf.can_create')
#     user_can_edit = request.user.has_perm('bookshelf.can_edit')
#     user_can_delete = request.user.has_perm('bookshelf.can_delete')
#
#     context = {
#         'books': books,
#         'user_can_create': user_can_create,
#         'user_can_edit': user_can_edit,
#         'user_can_delete': user_can_delete,
#     }
#     return render(request, 'bookshelf/book_list.html', context)

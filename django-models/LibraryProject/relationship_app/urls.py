# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView # Import new views

urlpatterns = [
    # Existing URLs from previous task
    path('books/', list_books, name='books_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # New: Authentication URLs
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
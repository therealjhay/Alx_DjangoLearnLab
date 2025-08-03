# LibraryProject/relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Existing URLs
    path('books/', views.list_books, name='books_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based access URLs
    path('admin-dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', views.member_view, name='member_dashboard'),

    # URLs for custom permissions (Book operations)
    path('books/add/', views.add_book, name='add_book/'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book/'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]

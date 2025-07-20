# LibraryProject/relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Existing URLs
    path('books/', views.list_books, name='books_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # New: Authentication URLs
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

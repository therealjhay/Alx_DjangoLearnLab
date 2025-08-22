from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    # 📄 List all posts
    path('posts/', PostListView.as_view(), name='post-list'),

    # 🆕 Create a new post
    path('posts/new/', PostCreateView.as_view(), name='post-create'),

    # 🔍 View a single post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # ✏️ Update a post
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),

    # ❌ Delete a post
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
]
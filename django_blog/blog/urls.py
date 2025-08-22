from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import search_posts, posts_by_tag

urlpatterns = [
    # 📄 List all posts
    path('posts/', PostListView.as_view(), name='post-list'),

    # 🆕 Create a new post
    path("posts/new/", PostCreateView.as_view(), name='post-create'),

    # 🔍 View a single post
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # ✏️ Update a post
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),

    # ❌ Delete a post
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),

    # 🔎 Search posts
    path('search/', search_posts, name='search-posts'),

    # 🏷️ Posts by tag
    path('tags/<str:tag_name>/', posts_by_tag, name='posts-by-tag'),

    # 💬 Comment URLs
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
["tags/<slug:tag_slug>/", "PostByTagListView.as_view()"]
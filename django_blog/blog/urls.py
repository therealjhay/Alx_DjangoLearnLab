from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

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
]

["post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"]


urlpatterns += [
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
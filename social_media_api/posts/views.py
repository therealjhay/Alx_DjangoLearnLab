from rest_framework import viewsets, permissions, status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from notifications.utils import create_notification
from django.shortcuts import get_object_or_404
from posts.serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__username']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk']).order_by('-created_at')

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)


class StandardResultsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsPagination

    def get_queryset(self):
        user = self.request.user
        followed_users = getattr(user, 'following', None)
        if followed_users is not None:
            followed_users = followed_users.all()
            return Post.objects.filter(author__in=followed_users).order_by('-created_at')
        return Post.objects.none()


#["Comment.objects.all()"]
#["Post.objects.filter(author__in=following_users).order_by", "following.all()"]

class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            # User has already liked, so unlike
            like.delete()
            return Response({"status": "unliked"}, status=status.HTTP_200_OK)
        else:
            # Create a notification for the post's author
            if post.author != user:
                create_notification(
                    recipient=post.author, 
                    actor=user, 
                    verb="liked your post", 
                    target=post
                )
            return Response({"status": "liked"}, status=status.HTTP_201_CREATED)
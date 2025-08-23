from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from django.urls import path
from .views import PostViewSet, CommentViewSet, PostFeedView, LikeView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')

posts_router = NestedSimpleRouter(router, 'posts', lookup='post')
posts_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = router.urls + posts_router.urls
urlpatterns = [
    path('feed/', PostFeedView.as_view(), name='post-feed'),
     path('posts/<int:pk>/like/', LikeView.as_view(), name='like-post'),
]
#["<int:pk>/unlike/"]
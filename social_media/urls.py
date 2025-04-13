from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import (
    UserViewSet, PostViewSet, CommentViewSet,
    LikeViewSet, FollowViewSet, UnfollowViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

users_router = NestedDefaultRouter(router, r'users', lookup='user')
users_router.register(r'follow', FollowViewSet, basename='user-follow')
users_router.register(r'unfollow', UnfollowViewSet, basename='user-unfollow')

posts_router = NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'like', LikeViewSet, basename='post-like')
posts_router.register(r'comment', CommentViewSet, basename='post-comment')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(posts_router.urls)),
    path('api/', include(users_router.urls)),
]

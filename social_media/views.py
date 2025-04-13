from rest_framework import mixins, status, permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

from .models import User, Post, Comment
from .serializers import (
    UserSerializer, UserDetailSerializer, PostSerializer, PostDetailSerializer, 
    CommentSerializer, LikeSerializer, FollowSerializer, UnfollowSerializer
)

class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        permission_classes = (permissions.IsAuthenticated,)
        return UserSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer
    
class CommentViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

@extend_schema_view(
    create=extend_schema(
        parameters=[
            OpenApiParameter("user_pk", type=int, location=OpenApiParameter.PATH),
            OpenApiParameter("post_pk", type=str, location=OpenApiParameter.PATH)
        ]
    )
)
class LikeViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,)

@extend_schema_view(
    create=extend_schema(
        parameters=[
            OpenApiParameter("user_pk", type=int, location=OpenApiParameter.PATH)
        ]
    )
)
class FollowViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

@extend_schema_view(
    create=extend_schema(
        parameters=[
            OpenApiParameter("user_pk", type=int, location=OpenApiParameter.PATH)
        ]
    )
)
class UnfollowViewSet(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UnfollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

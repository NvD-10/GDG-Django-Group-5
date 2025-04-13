from rest_framework.serializers import (ModelSerializer, StringRelatedField, SerializerMethodField, Serializer)
from .models import User, Post, Comment, Like, Follow

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio')

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio')

class CommentSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at')
        read_only_fields = ('id', 'user', 'created_at')

class LikeSerializer(Serializer):
    message = SerializerMethodField()
    
    def get_message(self) -> str:
        return "Post Liked"

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class PostDetailSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)
    likes = SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'created_at', 'updated_at', 'likes', 'comments')
    
    def get_likes(self, obj) -> int:
        return obj.like_set.count()
    
class FollowSerializer(Serializer):
    user = StringRelatedField()
    message = SerializerMethodField()
    
    def get_message(self, user=user) -> str:
        return f"You are now following {user}"

class UnfollowSerializer(Serializer):
    user = StringRelatedField()
    message = SerializerMethodField()
    
    def get_message(self, user=user) -> str:
        return f"You have unfollowed {user}"

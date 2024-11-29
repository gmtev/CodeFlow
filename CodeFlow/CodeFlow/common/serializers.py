from rest_framework import serializers
from CodeFlow.common.models import Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_id', 'author_username', 'content', 'created_at']
        read_only_fields = ['author', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'user_username', 'created_at']
        read_only_fields = ['user', 'created_at']
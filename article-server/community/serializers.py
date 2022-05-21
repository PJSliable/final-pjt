from rest_framework import serializers
from .models import Review, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'nickname')
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', ) # 'review',
        # read_only_fields = ('review', )


class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'rate', 'title', 'content', 'comments', 'like_users')

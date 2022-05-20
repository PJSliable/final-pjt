from rest_framework import serializers
from .models import Movie, Genre, Review, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Review
        fields = ('movie', 'like_users', 'rate', 'content', 'created_at', 'updated_at')


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

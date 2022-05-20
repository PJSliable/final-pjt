from rest_framework import serializers
from .models import Movie, Genre
from ..community.models import Review, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk','poster_path', 'title', 'vote_average',)
    

class ReviewListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('nickname')

    like_users = serializers.IntegerField(source='like_users.count', read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('user','like_users','rate', 'content','created_at', 'updated_at')

class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'vote_average','release_date', 'backdrop_path', 'genre_ids', 'overview', 'user', 'reviews')



from rest_framework import serializers
from .models import Movie, Genre
from community.models import Review
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
            fields = ('pk', 'username', 'nickname')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Review
        fields = ('user', 'like_users', 'rate', 'title')

class MovieDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'vote_average','release_date', 'backdrop_path', 'genre_ids', 'overview', 'reviews')



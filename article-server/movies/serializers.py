from rest_framework import serializers
from .models import Movie, Genre

import random

class MovieSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'vote_average',)
    

class MovieListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, default=lambda: random.sample(Genre.objects.all(), 3))
    movie = MovieSummarySerializer(many=True)
    class Meta:
        model = Genre
        fields = ('id', 'name', 'movie')
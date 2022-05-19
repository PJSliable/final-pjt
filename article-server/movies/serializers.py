from rest_framework import serializers
from .models import Movie, Genre



class MovieSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('poster_path', 'title', 'vote_average',)
    

from django.db import models
from django.conf import settings

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

# Create your models here.
class Movie(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='my_movies')

    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    # popularity = models.FloatField()
    # vote_count = models.IntegerField()
    vote_average = models.FloatField(null=True)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre, related_name='genres')
    backdrop_path = models.CharField(max_length=200)
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    rate = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
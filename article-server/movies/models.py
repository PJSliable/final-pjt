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
    vote_average = models.FloatField(null=True)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genre_ids = models.ManyToManyField(Genre, related_name='genres')
    backdrop_path = models.CharField(max_length=200)

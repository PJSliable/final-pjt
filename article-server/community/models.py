from django.db import models
from django.conf import settings
from movies.models import Movie

from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    rate = models.FloatField(
    validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

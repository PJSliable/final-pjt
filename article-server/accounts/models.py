from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True)
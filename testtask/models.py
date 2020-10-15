from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    likes = models.IntegerField(default=0)

class LikeAnalytics(models.Model):
    date = models.DateField()
    num_of_likes = models.IntegerField(default=0)

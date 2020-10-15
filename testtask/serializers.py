from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, LikeAnalytics


class LikeAnalyticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeAnalytics
        fields = ('date', 'num_of_likes')


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'text')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'text')

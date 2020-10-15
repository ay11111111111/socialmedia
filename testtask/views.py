from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, LikeAnalytics

from .serializers import (  PostCreateSerializer,
                            PostSerializer,
                            LikeAnalyticsSerializer
                            )
from .filters import LikeAnalyticsFilter
import datetime


class PostCreateView(viewsets.GenericViewSet):
    """
    APIView for creating new post.
    """
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated, )


    def create(self, request, format=None):
        user = request.user
        post = Post(author=user)
        serializer = self.serializer_class(post, data=request.data)
        data = {}
        if serializer.is_valid():
            post = serializer.save()
            data['response'] = 'successfully created new post'
            data['id'] = post.id
            data['author'] = post.author.username
            data['title'] = post.title
            data['text'] = post.text
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing posts.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostLikeView(viewsets.GenericViewSet):
    """
    APIView for leave like or unlike the post with id.
    """
    permission_classes = (IsAuthenticated, )
    queryset=''
    serializer_class = None

    @action(detail=True, methods=['put'])
    def like(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        post.likes += 1
        post.save()
        now = datetime.date.today()
        if LikeAnalytics.objects.filter(date=now):
            today_analytics = LikeAnalytics.objects.get(date=now)
            today_analytics.num_of_likes += 1
            today_analytics.save()
        else:
            LikeAnalytics.objects.create(date=now, num_of_likes=1)

        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def unlike(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if post.likes>0:
            post.likes -= 1
            post.save()

            now = datetime.date.today()
            if LikeAnalytics.objects.filter(date=now):
                today_analytics = LikeAnalytics.objects.get(date=now)
                today_analytics.num_of_likes -= 1
                today_analytics.save()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LikeAnalyticsView(ListAPIView):
    """
    APIView for viewing like analytics by day.
    """
    serializer_class = LikeAnalyticsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LikeAnalyticsFilter
    queryset = LikeAnalytics.objects.all()

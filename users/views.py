from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from .serializers import (UserSignUpSerializer,
                            UserActivitySerializer)
from .models import Profile
from datetime import datetime as dt

class UserCreateView(CreateAPIView):
    """
    APIView for creating new user.
    """
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSignUpSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user activities.
    """
    serializer_class = UserActivitySerializer
    queryset = User.objects.all()

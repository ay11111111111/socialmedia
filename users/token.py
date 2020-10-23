from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import update_last_login
from .models import Profile
from django.utils import timezone


def update_last_activity(user):
    profile = Profile.objects.get(user=user)
    profile.last_activity = timezone.now()
    profile.save()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        update_last_login(None, user)


        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        update_last_login(None, self.user)
        update_last_activity(self.user)

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

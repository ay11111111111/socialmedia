from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime as dt
from .models import Profile

class UserSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'password2')
        extra_kwargs = {
                'password':{'write_only': True}
        }

    def save(self):
        user = User(
                username=self.validated_data['username'],
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user

class UserActivitySerializer(serializers.ModelSerializer):
    last_activity = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username', 'last_login', 'last_activity')

    def get_last_activity(self, obj):
        profile = Profile.objects.get(user__id=obj.id)
        return profile.last_activity

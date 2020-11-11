from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer

# from app_calendar.models import User


User = get_user_model()


class UserSerializer(ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=50, min_length=4)
    first_name = serializers.CharField(max_length=50, min_length=4)
    last_name = serializers.CharField(max_length=50, min_length=4)

    user = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'password']

    def validate(self, attrs):
        email = attrs['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email', ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        self.user = User.objects.create_user(**validated_data)
        return self.user

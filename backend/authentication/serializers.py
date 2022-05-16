from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)
    username = serializers.CharField(max_length=100, read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'token',)

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again!')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact Admin')
        if not user.email_verified:
            raise AuthenticationFailed('Email not verified')

        return {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "token": user.token
        }

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
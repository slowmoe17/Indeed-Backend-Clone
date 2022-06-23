from dataclasses import fields
from pyexpat import model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from .models import User, EmployeeProfile, EmployerProfile
from rest_framework import serializers
from users.models import User


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)

        data["username"] = self.user.username
        data["email"] = self.user.email

        return data


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password", "gender", "country","account_type"]

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
            country=validated_data["country"],
            gender=validated_data["gender"],
            account_type=validated_data["account_type"],
            password=make_password(validated_data["password"]),
        )
        user.save()
        return user

class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = '__all__'

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = '__all__'
        
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(  # User 생성
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        # user.save()
        return user

    class Meta:
        model = User
        fields = ['email', 'name', 'password']


class IdCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError(
                {'email', ('해당 이메일은 이미 사용중입니다.')})
        return super().validate(attrs)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    tokens = serializers.CharField(max_length=300, read_only=True)

    class Meta:
        model = User
        fields = ['email, password', 'tokens']

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)
        user = authenticate(email=email, password=password)

        if user is None:
            return {
                'email': 'None'
            }

        update_last_login(None, user)

        return {
            'email': user.email,
            'tokens': user.tokens()

        }

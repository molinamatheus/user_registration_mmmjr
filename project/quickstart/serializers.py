from project.quickstart.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.CharField(required=True, allow_blank=False, max_length=100)
    password = serializers.CharField(required=False, allow_blank=True, min_length=6, max_length=100)
    birthday = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username) 
        instance.email = validated_data.get('email', instance.email) 
        instance.password = validated_data.get('password', instance.password) 
        instance.birthday = validated_data.get('birthday', instance.birthday) 
        instance.save()
        return instance
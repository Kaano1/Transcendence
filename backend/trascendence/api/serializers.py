from rest_framework import serializers
from .models.User import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "created_at", "updated_at", "username", "email"]

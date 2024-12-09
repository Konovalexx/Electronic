from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]

    def create(self, validated_data):
        # Проверка на существование пользователя с таким же username или email
        if User.objects.filter(username=validated_data["username"]).exists():
            raise serializers.ValidationError(
                {"username": "This username is already taken."}
            )
        if User.objects.filter(email=validated_data["email"]).exists():
            raise serializers.ValidationError(
                {"email": "This email is already registered."}
            )

        # Создание нового пользователя
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", ""),
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user

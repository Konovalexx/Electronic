from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer


# Вьюха для регистрации
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED,
            )

        # Добавлена обработка ошибок с более детализированным ответом
        return Response(
            {"error": "Invalid data", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


# Защищённый эндпоинт, доступный только аутентифицированным пользователям
class ProtectedView(APIView):
    permission_classes = [
        IsAuthenticated
    ]  # Только для аутентифицированных пользователей

    def get(self, request):
        return Response({"message": "You have access to this protected view!"})

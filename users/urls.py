from django.urls import path
from .views import RegisterView, ProtectedView  # Импортируем новый защищённый вид

urlpatterns = [
    path(
        "register/", RegisterView.as_view(), name="register"
    ),  # Регистрация пользователя
    path("protected/", ProtectedView.as_view(), name="protected"),  # Защищённый маршрут
]

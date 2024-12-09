from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Supplier, Product, NetworkNode
from .serializers import SupplierSerializer, ProductSerializer, NetworkNodeSerializer
from .filters import NetworkNodeFilter  # Импортируем фильтр
from .permissions import IsActiveUser  # Ваше кастомное разрешение


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [
        IsActiveUser
    ]  # Разрешаем доступ только активным пользователям

    def perform_update(self, serializer):
        # Запрещаем обновление задолженности
        # Удаляем 'debt' из данных, чтобы оно не было изменено
        validated_data = {
            key: value
            for key, value in serializer.validated_data.items()
            if key != "debt"
        }
        serializer.save(
            **validated_data
        )  # Сохраняем данные без изменения задолженности


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsActiveUser
    ]  # Разрешаем доступ только активным пользователям


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = (DjangoFilterBackend,)  # Указываем бэкенд для фильтрации
    filterset_class = NetworkNodeFilter  # Применяем фильтрацию через NetworkNodeFilter
    permission_classes = [
        IsActiveUser
    ]  # Ограничиваем доступ только активным пользователям

    @action(
        detail=False, methods=["post"], url_path="clear-debt", url_name="clear-debt"
    )
    def clear_debt(self, request):
        """
        Очищает задолженность перед поставщиком у выбранных объектов.
        Ожидает список ID объектов в теле запроса.
        """
        ids = request.data.get("ids", [])
        if not ids:
            return Response({"detail": "Не передан список ID объектов."}, status=400)

        # Проверяем, все ли ID существуют в базе
        nodes = NetworkNode.objects.filter(id__in=ids)
        if nodes.count() != len(ids):
            # Если количество найденных объектов меньше, чем переданных ID, возвращаем ошибку
            not_found_ids = set(ids) - set(nodes.values_list("id", flat=True))
            return Response(
                {
                    "detail": f'Не найдены объекты с ID: {", ".join(map(str, not_found_ids))}'
                },
                status=404,
            )

        # Обновляем задолженность
        nodes.update(debt=0)
        return Response(
            {"detail": f"Задолженность очищена для {nodes.count()} объектов."}
        )

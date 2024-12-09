import django_filters
from .models import NetworkNode


class NetworkNodeFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(
        lookup_expr="icontains"
    )  # Фильтрация по полю 'country'
    city = django_filters.CharFilter(
        lookup_expr="icontains"
    )  # Фильтрация по полю 'city'
    level = django_filters.ChoiceFilter(
        choices=NetworkNode.LEVEL_CHOICES
    )  # Фильтрация по уровню

    class Meta:
        model = NetworkNode
        fields = [
            "country",
            "city",
            "level",
        ]  # Добавляем дополнительные поля для фильтрации

from django.contrib import admin
from .models import Supplier, Product, NetworkNode
from .filters import NetworkNodeFilter  # Импортируем фильтр


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "country", "debt", "created_at"]
    search_fields = ["name", "country"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "model", "release_date"]
    search_fields = ["name", "model"]


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(self, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "supplier", "country", "debt", "created_at"]
    search_fields = ["name", "city", "supplier__name"]
    list_filter = [
        "city",
        "level",
        "supplier",
        "country",
    ]  # Добавлен фильтр по 'country'
    actions = [clear_debt]  # Добавлен action

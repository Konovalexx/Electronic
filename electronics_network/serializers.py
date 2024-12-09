from rest_framework import serializers
from .models import Supplier, Product, NetworkNode


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "debt",
            "created_at",
        ]
        read_only_fields = ["debt"]  # Запрещает изменение поля 'debt' через API


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "model", "release_date"]


class NetworkNodeSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = NetworkNode
        fields = [
            "id",
            "level",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "supplier",
            "debt",
            "created_at",
            "products",
        ]

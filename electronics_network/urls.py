from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, ProductViewSet, NetworkNodeViewSet

router = DefaultRouter()
router.register(r"suppliers", SupplierViewSet)
router.register(r"products", ProductViewSet)
router.register(r"networknodes", NetworkNodeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),  # Все маршруты будут начинаться с /api/
]

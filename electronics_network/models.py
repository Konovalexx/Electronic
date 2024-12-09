from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.model}"


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, "Factory"),
        (1, "Retail Network"),
        (2, "Individual Entrepreneur"),
    ]
    level = models.IntegerField(choices=LEVEL_CHOICES)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=100)  # Поле для фильтрации по стране
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    supplier = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="clients"
    )  # Ссылка на другой узел сети
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

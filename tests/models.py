"""Test models for SQL generation tests."""

from django.db import models


class Product(models.Model):
    """Sample model for testing ParadeDB search."""

    description = models.TextField()
    category = models.CharField(max_length=100)
    rating = models.IntegerField()
    in_stock = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict)

    class Meta:
        app_label = "tests"

    def __str__(self) -> str:
        return self.description[:50]

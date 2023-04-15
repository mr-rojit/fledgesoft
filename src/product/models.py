from django.db import models
from common.models import BaseModel


class Category(models.Model):
    name = models.CharField(verbose_name="Category name", max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(verbose_name="Product name", max_length=200)
    price = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)
    unit = models.CharField(max_length=30)
    stock_quantity = models.PositiveIntegerField(default=0)
    taxable = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


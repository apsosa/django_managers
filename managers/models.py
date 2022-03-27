from django.db import models
# Create your models here.
from managers.managers import OrderManager


class Product(models.Model):
    name = models.CharField(max_length=90)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=17, decimal_places=2)


class Order(models.Model):
    objects = OrderManager()
    number = models.CharField(max_length=30, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    # reference to objects in a different domain
    operator_id = models.IntegerField()
    customer_id = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='orders',
        on_delete=models.CASCADE
    )
    quantity = models.DecimalField(max_digits=19, decimal_places=3)
    price = models.DecimalField(max_digits=17, decimal_places=2)
    discount = models.DecimalField(
        max_digits=17,
        decimal_places=2,
        null=True,
        blank=True
    )

from django.db import models
from datetime import datetime  

from .enums import OrderStatus
class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=2, null=False, blank=False)
    qty_in_stcok = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'

class Order(models.Model):
    wanted_date = models.DateTimeField(default=datetime.now ,null=False, blank=False)
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PLANNED)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'order'

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'order_line'

    @property
    def price(self):
        return self.quantity * self.product.price


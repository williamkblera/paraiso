from django.db import models
from django.utils import timezone

class Order(models.Model):
    client = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.client

class ItemOrder(models.Model):
    order = models.ForeignKey(Order)
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):

        return str(self.order) + " - " + str(self.order.client)

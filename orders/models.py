from django.db import models

# Create your models here.
from core.models import Product


class Orders(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField()
    date_ordered = models.DateField(auto_now=True)
    delivered = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.product + str(self.quantity)

    class Meta:
        verbose_name_plural = 'orders'

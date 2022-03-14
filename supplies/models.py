from django.db import models

# Create your models here.
from core.models import Product


class Supplies(models.Model):
    Username = models.CharField(max_length=100)
    supplies = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    supply_date = models.DateField(auto_now=False)
    supplied = models.BooleanField(default=False, null=True,blank=True)

    def __str__(self):
        return self.Username + str(self.supplies)

    class Meta:
        verbose_name_plural = 'Supplies'


class Suppliers(models.Model):
    username = models.CharField(max_length=100)
    phone = models.BigIntegerField(default=0)
    address = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Suppliers'

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=False)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'


class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    total_sales = models.PositiveBigIntegerField()

    def __str__(self):
        return self.product

    class Meta:
        verbose_name_plural = 'Sales'




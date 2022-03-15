from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    inventory_quantitiy = models.DecimalField(max_digits=8, decimal_places=2)
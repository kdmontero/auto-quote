from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

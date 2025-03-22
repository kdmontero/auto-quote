from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField()
    sell_price = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)

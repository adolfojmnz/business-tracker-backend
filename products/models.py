from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    attributes = models.JSONField(blank=True, null=True)
    description = models.CharField(max_length=512, blank=True, null=True)
    cost = models.FloatField(default=0)
    price = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    unit = models.ForeignKey("products.Unit", on_delete=models.PROTECT)
    category = models.ForeignKey("products.Category", on_delete=models.PROTECT)
    added_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=32, unique=True)
    symbol = models.CharField(max_length=8, unique=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

from django.db import models


class Order(models.Model):
    class PaymentStatus(models.IntegerChoices):
        pending = 0
        processing = 1
        successful = 2
        failed = 3
        cancel = 4

    class OrderStatus(models.IntegerChoices):
        pending = 0
        delivered = 1
        picked = 2
        cancel = 3

    customer = models.ForeignKey("customers.Customer", on_delete=models.PROTECT)
    payment_status = models.IntegerField(choices=PaymentStatus.choices)
    order_status = models.IntegerField(choices=OrderStatus.choices)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}'s order"


class OrderItem(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product_attributes = models.JSONField(blank=True)
    quantity = models.IntegerField(default=1)
    subtotal = models.FloatField(blank=True)

    def calculate_subtotal(self):
        self.subtotal = self.quantity * self.product.price

    def generate_product_attributes(self):
        attributes = {
            "name": self.product.name,
            "cost": self.product.cost,
            "price": self.product.price,
            "stock": f"{self.product.stock} {self.product.unit.symbol}"
        }
        self.product_attributes = attributes

    def save(self, *args, **kwargs):
        self.calculate_subtotal()
        self.generate_product_attributes()
        return super().save(*args, **kwargs)

    class Meta:
        unique_together = ["product", "order"]

from django.db.models import Sum

from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from orders.models import Order, OrderItem


class OrderSerializer(ModelSerializer):
    customer_full_name = SerializerMethodField()
    total = SerializerMethodField()

    def get_customer_full_name(self, order):
        customer = order.customer
        return f"{customer.first_name} {customer.last_name}"

    def get_total(self, order):
        return order.orderitem_set.aggregate(
            Sum("subtotal")
        )["subtotal__sum"]

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    product_price = SerializerMethodField()
    product_unit = SerializerMethodField()

    def get_product_name(self, order_item):
        return order_item.product.name

    def get_product_price(self, order_item):
        return order_item.product_attributes.get("price")

    def get_product_unit(self, order_item):
        return order_item.product_attributes.get("unit")

    class Meta:
        model = OrderItem
        fields = "__all__"

from django.db.models import Sum, Max, Min, Avg

from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from customers.models import Customer

from orders.models import OrderItem


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerAnalyticsSerializer(ModelSerializer):
    total_spent = SerializerMethodField()
    total_orders = SerializerMethodField()
    total_revenue = SerializerMethodField()
    largest_order = SerializerMethodField()
    smallest_order = SerializerMethodField()
    average_order = SerializerMethodField()
    top_products = SerializerMethodField()
    latest_orders = SerializerMethodField()

    def get_customer_orders(self, customer):
        PAYMENT_SUCCESSFUL = 2
        return customer.order_set.filter(
            payment_status=PAYMENT_SUCCESSFUL
        )

    def get_customer_orderitems(self, customer):
        PAYMENT_SUCCESSFUL = 2
        return OrderItem.objects.filter(
            order__customer=customer,
            order__payment_status=PAYMENT_SUCCESSFUL
        )

    def get_total_orders(self, customer):
        return self.get_customer_orders(customer).count()

    def get_total_spent(self, customer):
        return self.get_customer_orderitems(customer).aggregate(
            Sum("subtotal")
        )["subtotal__sum"]

    def get_total_revenue(self, customer):
        return round(self.get_customer_orderitems(customer).aggregate(
            Sum("revenue")
        )["revenue__sum"] or 0, 2)

    def get_largest_order(self, customer):
        return round(self.get_customer_orderitems(customer).values().aggregate(
            Max("subtotal")
        )["subtotal__max"] or 0, 2)

    def get_smallest_order(self, customer):
        return round(self.get_customer_orderitems(customer).values().aggregate(
            Min("subtotal")
        )["subtotal__min"] or 0, 2)

    def get_average_order(self, customer):
        return round(self.get_customer_orderitems(customer).values().aggregate(
            Avg("subtotal")
        )["subtotal__avg"] or 0, 2)

    def get_top_products(self, customer):
        return (
            self.get_customer_orderitems(customer).values(
                "product_id",
                "product__name",
            )
            .annotate(total_purchased=Sum("quantity"))
            .annotate(total_spent=Sum("subtotal"))
            .annotate(total_revenue=Sum("revenue"))
            .annotate(last_purchased=Max("order__datetime"))
            .order_by("-total_purchased")[:5]
        )

    def get_latest_orders(self, customer):
        return (
            self.get_customer_orderitems(customer).values(
                "order",
                "order__payment_status",
                "order__order_status",
                "order__datetime",
            )
            .annotate(order__total=Sum("subtotal"))
            .order_by("-order__datetime")[:5]
        )

    class Meta:
        model = Customer
        fields = [
            "total_spent",
            "total_orders",
            "total_revenue",
            "largest_order",
            "smallest_order",
            "average_order",
            "top_products",
            "latest_orders",
        ]

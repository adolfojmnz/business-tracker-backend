from django.db.models import Sum, Max, Min, Avg

from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from products.models import Product, Category, Unit


class ProductSerializer(ModelSerializer):
    unit_symbol = SerializerMethodField()
    category_name = SerializerMethodField()

    def get_unit_symbol(self, product):
        return product.unit.symbol

    def get_category_name(self, product):
        return product.category.name

    class Meta:
        model = Product
        fields = "__all__"


class ProductAnaliticsSerializer(ModelSerializer):
    total_sold = SerializerMethodField()
    total_revenue = SerializerMethodField()
    total_customers = SerializerMethodField()
    max_order_quantity = SerializerMethodField()
    min_order_quantity = SerializerMethodField()
    avg_order_quantity = SerializerMethodField()
    top_customers = SerializerMethodField()
    latest_purchases = SerializerMethodField()
    unit_symbol = SerializerMethodField()

    def get_orderitems(self, product):
        PAYMENT_SUCCESSFUL = 2
        return product.orderitem_set.filter(
            order__payment_status=PAYMENT_SUCCESSFUL
        )

    def get_total_sold(self, product):
        return self.get_orderitems(product).aggregate(
            Sum("quantity")
        )["quantity__sum"] or 0

    def get_total_revenue(self, product):
        return round(self.get_orderitems(product).aggregate(
            Sum("revenue")
        )["revenue__sum"] or 0, 2)

    def get_total_customers(self, product):
        return self.get_orderitems(product).values(
            "order__customer"
        ).distinct().count() or 0

    def get_max_order_quantity(self, product):
        return self.get_orderitems(product).aggregate(
            Max("quantity")
        )["quantity__max"] or 0

    def get_min_order_quantity(self, product):
        return self.get_orderitems(product).aggregate(
            Min("quantity")
        )["quantity__min"] or 0

    def get_avg_order_quantity(self, product):
        return round(self.get_orderitems(product).aggregate(
            Avg("quantity")
        )["quantity__avg"] or 0, 2)

    def get_top_customers(self, product):
        return (
            self.get_orderitems(product).values(
                "order__customer",
                "order__customer__first_name",
                "order__customer__last_name",
            )
            .annotate(total_quantity=Sum("quantity"))
            .annotate(last_purchased=Max("order__datetime"))
            .order_by("-total_quantity")[:3]
        )

    def get_latest_purchases(self, product):
        return (
            self.get_orderitems(product).values(
                "order__customer",
                "order__customer__first_name",
                "order__customer__last_name",
                "quantity",
            )
            .annotate(datetime=Max("order__datetime"))
            .order_by("-datetime")[:3]
        )

    def get_unit_symbol(self, product):
        return product.unit.symbol

    class Meta:
        model = Product
        fields = [
            "total_sold",
            "total_revenue",
            "total_customers",
            "max_order_quantity",
            "min_order_quantity",
            "avg_order_quantity",
            "top_customers",
            "latest_purchases",
            "unit_symbol",
        ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

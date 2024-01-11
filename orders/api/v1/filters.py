from django_filters import rest_framework as filters

from orders.models import Order, OrderItem


class FilterBackend(filters.DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)

        if hasattr(view, "get_filterset_kwargs"):
            kwargs.update(view.get_filterset_kwargs())

        return kwargs


class OrderFilterSet(filters.FilterSet):
    customer = filters.NumberFilter(
        field_name="customer__pk", lookup_expr="exact",
    )
    payment_status = filters.NumberFilter(
        field_name="payment_status", lookup_expr="exact",
    )
    order_status = filters.NumberFilter(
        field_name="order_status", lookup_expr="exact",
    )
    datetime = filters.DateTimeFilter(
        field_name="datetime", lookup_expr="exact",
    )
    date = filters.DateFilter(
        field_name="datetime__date", lookup_expr="exact",
    )
    year = filters.DateFilter(
        field_name="datetime__date__year", lookup_expr="exact",
    )
    month = filters.DateFilter(
        field_name="datetime__date__month", lookup_expr="exact",
    )

    class Meta:
        model = Order
        fields = "__all__"


class OrderItemFilterSet(filters.FilterSet):
    product = filters.NumberFilter(
        field_name="customer__pk", lookup_expr="exact",
    )
    product_name = filters.CharFilter(
        field_name="product__name", lookup_expr="icontains"
    )
    order = filters.NumberFilter(
        field_name="order__pk", lookup_expr="exact",
    )
    customer = filters.NumberFilter(
        field_name="order__customer__pk", lookup_expr="exact",
    )
    customer_first_name = filters.CharFilter(
        field_name="order__customer__fist_name", lookup_expr="icontains"
    )

    class Meta:
        model = OrderItem
        fields = [
            "product",
            "product_name",
            "order",
            "customer",
            "customer_first_name",
        ]

from django_filters import rest_framework as filters

from products.models import Product


class FilterBackend(filters.DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)

        if hasattr(view, "get_filterset_kwargs"):
            kwargs.update(view.get_filterset_kwargs())

        return kwargs


class ProductFilterSet(filters.FilterSet):
    name = filters.CharFilter(
        "name",
        lookup_expr="icontains",
    )
    category = filters.NumberFilter(
        "category__pk",
        lookup_expr="exact",
    )
    cost_gte = filters.NumberFilter(
        "cost",
        lookup_expr="gte",
    )
    cost_lte = filters.NumberFilter(
        "cost",
        lookup_expr="lte",
    )
    price_gte = filters.NumberFilter(
        "price",
        lookup_expr="gte",
    )
    price_lte = filters.NumberFilter(
        "price",
        lookup_expr="lte",
    )

    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "cost_gte",
            "cost_lte",
            "price_gte",
            "price_lte",
        ]

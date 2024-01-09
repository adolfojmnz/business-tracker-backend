from django_filters import rest_framework as filters

from customers.models import Customer


class FilterBackend(filters.DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)

        if hasattr(view, "get_filterset_kwargs"):
            kwargs.update(view.get_filterset_kwargs())

        return kwargs


class CustomerFilterSet(filters.FilterSet):
    alias = filters.CharFilter(
        "alias", lookup_expr="icontains",
    )
    first_name = filters.CharFilter(
        "first_name", lookup_expr="icontains",
    )
    last_name = filters.CharFilter(
        "last_name", lookup_expr="icontains",
    )
    id_card = filters.NumberFilter(
        "id_card", lookup_expr="exact",
    )
    email = filters.NumberFilter(
        "email", lookup_expr="icontains",
    )
    phone = filters.CharFilter(
        "phone", lookup_expr="icontains",
    )

    class Meta:
        model = Customer
        fields = [
            "alias",
            "first_name",
            "last_name",
            "id_card",
            "email",
            "phone",
        ]

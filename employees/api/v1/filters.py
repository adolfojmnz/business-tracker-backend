from django_filters import rest_framework as filters

from employees.models import Employee, EmployeeContract


class FilterBackend(filters.DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        kwargs = super().get_filterset_kwargs(request, queryset, view)

        if hasattr(view, "get_filterset_kwargs"):
            kwargs.update(view.get_filterset_kwargs())

        return kwargs


class EmployeeFilterSet(filters.FilterSet):
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
    is_employed = filters.BooleanFilter(
        "is_employed"
    )

    class Meta:
        model = Employee
        fields = [
            "first_name",
            "last_name",
            "id_card",
            "email",
            "phone",
            "is_employed",
        ]


class EmployeeContractFilterSet(filters.FilterSet):
    employee = filters.NumberFilter(
        "employee", lookup_expr="exact",
    )
    name = filters.CharFilter(
        "name", lookup_expr="icontains",
    )
    type = filters.CharFilter(
        "type", "iexact",
    )
    start_date = filters.DateFilter(
        "start_date", lookup_expr="exact",
    )
    start_year = filters.DateFilter(
        "start_date__year", lookup_expr="exact",
    )
    start_month = filters.DateFilter(
        "start_date__month", lookup_expr="exact",
    )

    class Meta:
        model = EmployeeContract
        fields = [
            "employee",
            "name",
            "type",
            "start_date",
            "start_year",
            "start_month",
        ]

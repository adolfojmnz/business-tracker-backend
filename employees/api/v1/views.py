from rest_framework.permissions import (
    IsAdminUser,
    SAFE_METHODS,
    IsAuthenticated,
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from employees.models import Employee, EmployeeContract
from employees.api.v1.serializers import (
    EmployeeSerializer,
    EmployeeContractSerializer,
)

from employees.api.v1.filters import (
    FilterBackend,
    EmployeeFilterSet,
    EmployeeContractFilterSet,
)


class PermissionsMixin:
    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        if self.request.method not in SAFE_METHODS:
            self.permissions_classes = [IsAdminUser]
        return super().get_permissions()


class EmployeeListView(PermissionsMixin, ListCreateAPIView):
    model = Employee
    queryset = model.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [FilterBackend]
    filterset_class = EmployeeFilterSet


class EmployeeDetailsView(PermissionsMixin, RetrieveUpdateAPIView):
    model = Employee
    queryset = model.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [FilterBackend]
    filterset_class = EmployeeFilterSet


class EmployeeContractListView(PermissionsMixin, ListCreateAPIView):
    model = EmployeeContract
    queryset = model.objects.all()
    serializer_class = EmployeeContractSerializer
    filter_backends = [FilterBackend]
    filterset_class = EmployeeContractFilterSet


class EmployeeContractDetailsView(PermissionsMixin, RetrieveUpdateAPIView):
    model = Employee
    queryset = model.objects.all()
    serializer_class = EmployeeContractSerializer
    filter_backends = [FilterBackend]
    filterset_class = EmployeeContractFilterSet

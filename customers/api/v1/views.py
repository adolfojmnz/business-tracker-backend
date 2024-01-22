from rest_framework.permissions import (
    IsAdminUser,
    SAFE_METHODS,
    IsAuthenticated,
)
from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)

from customers.models import Customer
from customers.api.v1.serializers import (
    CustomerSerializer,
    CustomerAnalyticsSerializer,
)
from customers.api.v1.filters import FilterBackend, CustomerFilterSet


class PermissionsMixin:
    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class CustomerListView(PermissionsMixin, ListCreateAPIView):
    model = Customer
    queryset = model.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [FilterBackend]
    filterset_class = CustomerFilterSet


class CustomerDetailsView(PermissionsMixin, RetrieveUpdateAPIView):
    model = Customer
    queryset = model.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [FilterBackend]
    filterset_class = CustomerFilterSet


class CustomerAnalyticsView(PermissionsMixin, RetrieveAPIView):
    model = Customer
    queryset = model.objects.all()
    serializer_class = CustomerAnalyticsSerializer

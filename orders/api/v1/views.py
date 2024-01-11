from rest_framework.permissions import (
    IsAdminUser,
    SAFE_METHODS,
    IsAuthenticated,
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)

from orders.models import Order, OrderItem
from orders.api.v1.serializers import (
    OrderSerializer,
    OrderItemSerializer,
)
from orders.api.v1.filters import (
    FilterBackend,
    OrderFilterSet,
    OrderItemFilterSet,
)


class PermissionsMixin:
    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class OrderListView(PermissionsMixin, ListCreateAPIView):
    model = Order
    queryset = model.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [FilterBackend]
    filterset_class = OrderFilterSet


class OrderDetailsView(PermissionsMixin, RetrieveUpdateAPIView):
    model = Order
    queryset = model.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [FilterBackend]
    filterset_class = OrderFilterSet


class OrderItemListView(PermissionsMixin, ListCreateAPIView):
    model = OrderItem
    queryset = model.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [FilterBackend]
    filterset_class = OrderItemFilterSet


class OrderItemDetailsView(PermissionsMixin, RetrieveUpdateAPIView):
    model = OrderItem
    queryset = model.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [FilterBackend]
    filterset_class = OrderItemFilterSet

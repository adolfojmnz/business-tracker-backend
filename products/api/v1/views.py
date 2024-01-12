from rest_framework.permissions import (
    SAFE_METHODS,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)

from products.models import Product, Category, Unit
from products.api.v1.serializers import (
    UnitSerializer,
    ProductSerializer,
    CategorySerializer,
    ProductAnaliticsSerializer,
)

from products.api.v1.filters import (
    FilterBackend,
    ProductFilterSet,
)


class PermissionsMixin:
    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class ProductListView(ListCreateAPIView, PermissionsMixin):
    model = Product
    queryset = model.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [FilterBackend]
    filterset_class = ProductFilterSet


class ProductDetailsView(RetrieveUpdateAPIView, PermissionsMixin):
    model = Product
    queryset = model.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [FilterBackend]
    filterset_class = ProductFilterSet


class ProductAnaliticsView(RetrieveAPIView, PermissionsMixin):
    model = Product
    queryset = model.objects.all()
    serializer_class = ProductAnaliticsSerializer


class CategoryListView(ListCreateAPIView, PermissionsMixin):
    model = Category
    queryset = model.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailsView(RetrieveUpdateAPIView, PermissionsMixin):
    model = Category
    queryset = model.objects.all()
    serializer_class = CategorySerializer


class UnitListView(ListCreateAPIView, PermissionsMixin):
    model = Unit
    queryset = model.objects.all()
    serializer_class = UnitSerializer


class UnitDetailsView(RetrieveUpdateAPIView, PermissionsMixin):
    model = Unit
    queryset = model.objects.all()
    serializer_class = UnitSerializer

from rest_framework.serializers import ModelSerializer, SerializerMethodField

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


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

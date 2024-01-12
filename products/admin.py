from django.contrib import admin

from products.models import Product, Unit, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "cost",
        "price",
        "stock",
        "unit",
        "category",
        "added_on",
        "last_updated",
    ]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "symbol",
        "description",
        "added_on",
        "last_updated",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "description",
        "added_on",
        "last_updated",
    ]

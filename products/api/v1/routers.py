from django.urls import path

from products.api.v1 import views


urlpatterns = [
    path(
        "products",
        views.ProductListView.as_view(),
        name="product-list",
    ),
    path(
        "products/<int:pk>",
        views.ProductDetailsView.as_view(),
        name="product-details",
    ),
    path(
        "categories",
        views.CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "category/<int:pk>",
        views.CategoryDetailsView.as_view(),
        name="category-details",
    ),
    path(
        "units",
        views.UnitListView.as_view(),
        name="unit-list",
    ),
    path(
        "units/<int:pk>",
        views.UnitDetailsView.as_view(),
        name="unit-details",
    ),
]

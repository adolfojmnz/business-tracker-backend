from django.urls import path

from orders.api.v1 import views


urlpatterns = [
    path(
        "orders",
        views.OrderListView.as_view(),
        name="order-list",
    ),
    path(
        "orders/<int:pk>",
        views.OrderDetailsView.as_view(),
        name="order-details",
    ),
    path(
        "order-items",
        views.OrderItemListView.as_view(),
        name="order-item-list",
    ),
    path(
        "order-items/<int:pk>",
        views.OrderItemDetailsView.as_view(),
        name="order-item-details",
    ),
]

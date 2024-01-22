from django.urls import path

from customers.api.v1 import views


urlpatterns = [
    path(
        "customers",
        views.CustomerListView.as_view(),
        name="customer-list",
    ),
    path(
        "customers/<int:pk>",
        views.CustomerDetailsView.as_view(),
        name="customer-details",
    ),
    path(
        "customers/<int:pk>/analytics",
        views.CustomerAnalyticsView.as_view(),
        name="customer-analytics",
    )
]

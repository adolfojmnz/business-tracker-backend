from django.urls import path

from employees.api.v1 import views


urlpatterns = [
    path(
        "employees",
        views.EmployeeListView.as_view(),
        name="employee-list",
    ),
    path(
        "employees/<int:pk>",
        views.EmployeeDetailsView.as_view(),
        name="employee-details",
    ),
    path(
        "employee-contracts",
        views.EmployeeContractListView.as_view(),
        name="employee-contract-list",
    ),
    path(
        "employee-contracts/<int:pk>",
        views.EmployeeContractDetailsView.as_view(),
        name="employee-contract-details",
    ),
]

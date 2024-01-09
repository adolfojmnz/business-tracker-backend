from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tokens.routers")),
    path("api/", include("accounts.api.routers")),
    path("api/v1/", include("products.api.v1.routers")),
    path("api/v1/", include("customers.api.v1.routers")),
    path("api/v1/", include("employees.api.v1.routers")),
]

from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "alias",
        "first_name",
        "last_name",
        "id_card",
        "email",
        "phone",
        "added_on",
    ]

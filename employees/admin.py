from django.contrib import admin

from employees.models import Employee, EmployeeContract


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "id_card",
        "email",
        "phone",
        "is_employed",
    ]


@admin.register(EmployeeContract)
class EmployeeContractAdmin(admin.ModelAdmin):
    list_display = [
        "employee",
        "type",
        "monthly_salary",
        "monthly_bonus",
        "yearly_bonus",
        "start_date",
        "end_date",
    ]

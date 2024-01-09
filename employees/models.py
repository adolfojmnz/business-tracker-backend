from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    id_card = models.IntegerField(unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, unique=True)
    is_employed = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + self.last_name


class EmployeeContract(models.Model):
    CONTRACT_TYPE = [
        ("FT", "Full Time"),
        ("PT", "Part Time"),
        ("WE", "Weekends"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    name = models.CharField(max_length=128)
    type = models.CharField(choices=CONTRACT_TYPE, max_length=2)
    monthly_salary = models.FloatField()
    monthly_bonus = models.FloatField(blank=True, null=True)
    yearly_bonus = models.FloatField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee.first_name} | {self.name[:64]}"

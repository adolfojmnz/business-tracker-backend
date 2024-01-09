from rest_framework.serializers import ModelSerializer

from employees.models import Employee, EmployeeContract


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeContractSerializer(ModelSerializer):
    class Meta:
        model = EmployeeContract
        fields = "__all__"

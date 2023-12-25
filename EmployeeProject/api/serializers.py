from rest_framework import serializers
from .models import Company, Employee

class CompanySerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['company_id','company_name','company_address','created_at','updated_at','is_active']

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id','company_id','employee_name','employee_contact','employee_address','created_at','updated_at', 'is_active']
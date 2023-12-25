from . models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
      name = serializers.CharField(max_length=100)
      email = serializers.EmailField()
      password = serializers.IntegerField()
      phone = serializers.IntegerField()
    
      def create(self, validated_data):
          return Employee.objects.create(**validated_data)
    
      def update(self  , employee , validated_data):
          newEmployee = Employee(**validated_data)
          newEmployee.id = employee.id
          newEmployee.save()
          return newEmployee
          
         
    
class UserSerializer(serializers.Serializer):
      username = serializers.CharField(max_length=30)
      email = serializers.EmailField()
      password = serializers.IntegerField()
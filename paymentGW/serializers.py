from rest_framework import serializers
from . models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Employee
        fields = ('id', 'name', 'department', 'join_date', 'profile_photo')
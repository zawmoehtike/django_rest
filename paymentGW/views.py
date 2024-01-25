from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from . models import Department, Employee
from . serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request, id = None):
    if request.method == "GET":
        departmentsModel = Department.objects.all()
        departmentsSerializer = DepartmentSerializer(departmentsModel, many = True)
        return JsonResponse(departmentsSerializer.data, safe = False)
    
    elif request.method == "POST":
        departmentRequest = JSONParser().parse(request)
        departmentSerializer = DepartmentSerializer(data = departmentRequest)

        if(departmentSerializer.is_valid()):
            departmentSerializer.save()
            return JsonResponse("Department is added successfully", safe = False)
        else:
            return JsonResponse("Failed to add department", safe = False)

    elif request.method == "PUT":
        departmentRequest = JSONParser().parse(request)
        departmentModel = Department.objects.get(id = departmentRequest['id'])
        departmentSerializer = DepartmentSerializer(departmentModel, data = departmentRequest)

        if(departmentSerializer.is_valid()):
            departmentSerializer.save()
            return JsonResponse("Department is updated successfully", safe = False)
        else:
            return JsonResponse("Failed to update department", safe = False)

    elif request.method == "DELETE":
        try:
            departmentModel = Department.objects.get(id = id)
            departmentModel.delete()
            return JsonResponse("Department is deleted successfully", safe = False)
        except Exception as e:
            return JsonResponse(f"Error deleting department: {str(e)}", status = 500, safe = False)





@csrf_exempt
def employeeApi(request, employeeID = None):
    if request.method == "GET":
        employeesModel = Employee.objects.all()
        employeesSerializer = EmployeeSerializer(employeesModel, many = True)
        return JsonResponse(employeesSerializer.data, safe = False)
    
    elif request.method == "POST":
        employeeRequest = JSONParser().parse(request)
        employeeSerializer = EmployeeSerializer(data = employeeRequest)

        if(employeeSerializer.is_valid()):
            employeeSerializer.save()
            return JsonResponse("Employee is added successfully", safe = False)
        else:
            return JsonResponse("Failed to add employee", safe = False)

    elif request.method == "PUT":
        employeeRequest = JSONParser().parse(request)
        employeeModel = Employee.objects.get(id = employeeRequest['id'])
        employeeSerializer = EmployeeSerializer(employeeModel, data = employeeRequest)

        if(employeeSerializer.is_valid()):
            employeeSerializer.save()
            return JsonResponse("Employee is updated successfully", safe = False)
        else:
            return JsonResponse("Failed to update employee", safe = False)

    elif request.method == "DELETE":
        try:
            employeeModel = Employee.objects.get(id = employeeID)
            employeeModel.delete()
            return JsonResponse("Employee is deleted successfully", safe = False)
        except Exception as e:
            return JsonResponse(f"Error deleting employee: {str(e)}", status = 500, safe = False)
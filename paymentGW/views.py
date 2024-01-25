from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from . models import Department, Employee
from . serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request, deptID = None):
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
            departmentModel = Department.objects.get(id=deptID)
            departmentModel.delete()
            return JsonResponse("Department is deleted successfully", safe = False)
        except Exception as e:
            return JsonResponse(f"Error deleting department: {str(e)}", status = 500, safe = False)
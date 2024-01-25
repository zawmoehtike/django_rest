
from django.urls import path, include
from . views import departmentApi, employeeApi

urlpatterns = [
    path('department', departmentApi),
    path('department/<int:id>', departmentApi),

    path('employee', employeeApi),
    path('employee/<int:employeeID>', employeeApi),
]
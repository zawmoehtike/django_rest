
from django.urls import path, include
from . import views

urlpatterns = [
    path('department', views.departmentApi),
    path('department/<int:deptID>', views.departmentApi),
]
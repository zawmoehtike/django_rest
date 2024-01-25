
from django.urls import path, include
from . views import departmentApi, employeeApi, saveProfilePhotoFile

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department', departmentApi),
    path('department/<int:id>', departmentApi),

    path('employee', employeeApi),
    path('employee/<int:employeeID>', employeeApi),

    path('employee/upload_profile_photo', saveProfilePhotoFile)
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
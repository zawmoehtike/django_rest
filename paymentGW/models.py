from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    department = models.CharField(max_length=300)
    join_date = models.CharField(max_length=300)
    profile_photo = models.CharField(max_length=300)


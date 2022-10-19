from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=500)

class Employee(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=500)
    Phone=models.CharField(max_length=20)
    Email=models.EmailField(max_length=500)
    Department=models.CharField(max_length=500)
    Salary=models.CharField(max_length=15, null=True, blank=True)
    Datejoining=models.DateTimeField()
    Dept=models.ForeignKey(Departments, on_delete=models.CASCADE, null=True, blank=True)
    Photo=models.CharField(max_length=500)


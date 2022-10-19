from django.contrib import admin
from. views import Employee, Departments

# Register your models here.
admin.site.register(Departments)
admin.site.register(Employee)

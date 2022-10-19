from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import generics
from .models import Departments, Employee
from rest_framework import status, viewsets
from django .contrib.auth.models import User
from. serializers import DepartmentSerializer, EmployeeSerializer, UserSerializer, RegisterSerializer
from django.core.files.storage import default_storage
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your views here.
class DepartmentApi(viewsets.ModelViewSet):
    queryset=Departments.objects.all()
    serializer_class=DepartmentSerializer
   

class EmployeeApi(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    

   
class UserApi(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=(AuthToken,)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return  JsonResponse(file_name, safe=False)

@csrf_exempt
def EmployeeFilterApi(request, value=''):
    if request.method=='GET':
        employees=Employee.objects.filter(EmployeeName__icontains=value)
        employees_serializer=EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


def EmployeeOrderApi(request, value):
    if request.method=='GET':
        employees=Employee.objects.order_by(value)
        employees_serializer=EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

"""
@csrf_exempt
def departmentApi(request, id=0):
    if request.method=='GET':
        departments=Department.objects.all()
        departments_serializer=DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Added succefully', safe=False )
        return JsonResponse('Failed to add', safe=False )
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department.data, safe=False)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('updated succesfully', safe=False)
        return JsonResponse('faild to update', safe=False)

    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        return JsonResponse('Deleted successfully', safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method=='GET':
        employees=Employee.objects.all()
        employees_serializer=EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('Added succefully', safe=False )
        return JsonResponse('Failed to add', safe=False )
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employee.objects.get(EmployeeId=employee_data['DepartmentId'])
        employees_serializer=EmployeeSerializer(employee.data, safe=False)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse('updated succesfully', safe=False)
        return JsonResponse('faild to update', safe=False)

    elif request.method=='DELETE':
        employee=Employee.objects.get(DepartmentId=id)
        return JsonResponse('Deleted successfully', safe=False)

 """
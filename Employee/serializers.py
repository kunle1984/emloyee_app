from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Employee, Departments
from django .contrib.auth.models import User
from knox.models import AuthToken

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId', 'DepartmentName',)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=('EmployeeId', 'EmployeeName', 'Phone','Salary', 'Email', 'Department','Dept', 'Datejoining', 'Photo', )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['username', 'password', 'email']
        #To make sure that the password is not displayed and to encrypt the passwod
        extra_kwargs={'password':{
            'write_only':True,
            'required':True
        }
        }
    def create(self, validated_data):
            user=User.objects.create_user(**validated_data)
            #creating token
            AuthToken.objects.create(user=user)
            return user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


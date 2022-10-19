from django.urls import path,include, re_path
from .views import DepartmentApi, EmployeeApi, SaveFile, EmployeeFilterApi, EmployeeOrderApi, UserApi, RegisterAPI, LoginAPI
from knox import views as knox_views
from rest_framework.routers import DefaultRouter

from django.conf import settings
router=DefaultRouter()
router.register('departments', DepartmentApi, basename='departments')
router.register('employees', EmployeeApi, basename='employees')
router.register('users', UserApi, basename='users')
 
urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('', include(router.urls)),
    #path('departments/', DepartmentApi.as_view({'get':'list'}), name='department'),
    #re_path(r'^department/([0-9]+)$', DepartmentApi.as_view({'get':'list'}), name='departments'),
    #path('department', departmentApi, name='department'),
    path('employeefilter/<str:value>', EmployeeFilterApi, name='employeefilter'),
    path('employeeorder/<str:value>', EmployeeOrderApi, name='employeeorder'),
    re_path(r'^employee/savefile', SaveFile),
    
   
    
]

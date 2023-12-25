from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee', views.employee, name='home'),
    path('employee/<int:pk>', views.employeeDetail,name='employee'),
    path('users', views.user, name='home'),
]

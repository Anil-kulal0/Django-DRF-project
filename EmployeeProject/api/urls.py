from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# router = DefaultRouter()

# router.register(r'companies',views.CompanyViewSet)
# router.register(r'employies',views.EmployeeViewSet)

urlpatterns = [
  
    # path('', include(router.urls)),
    
    path('company/', views.company_list),
    path('company/<int:pk>/', views.company_detail),
    path('employee/', views.employee_list),
    path('employee/<int:pk>/', views.employee_detail),
]


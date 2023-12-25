from django.contrib import admin
from .models import Company, Employee
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id','company_name','company_address','created_at','updated_at','is_active']
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id','company_id','employee_name','employee_contact','employee_address','created_at','updated_at','is_active']
from django.utils.translation import gettext as _
from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True, auto_created=True)
    company_name = models.CharField(_("Name"), max_length=50)
    company_address = models.TextField(_("Address"))
    created_at = models.DateTimeField(_("Create At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    is_active = models.BooleanField(_("Status"), default=True)

    def __str__(self) -> str:
        return self.company_name

    class Meta:
        ordering = ['created_at']
        

class Employee(models.Model):
    employee_id = models.AutoField(_("Employee ID"), primary_key=True, auto_created=True)
    company_id = models.ForeignKey(Company, verbose_name=_("Company ID"), on_delete=models.CASCADE)
    employee_name = models.CharField(_("Employee Name"),max_length=50)
    employee_contact = models.BigIntegerField(_("Employee Contact"))
    employee_address = models.TextField(_("Employee Addres"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_(""), auto_now=True)
    is_active = models.BooleanField(_("Status"), default=True)
    
    def __str__(self) -> str:
        return self.employee_name
    
    class Meta:
        ordering = ['created_at']
from django.contrib import admin
from .models import Deparment, Role, Employee 
# Register your models here.
admin.site.register(Deparment)
admin.site.register(Role)
admin.site.register(Employee)
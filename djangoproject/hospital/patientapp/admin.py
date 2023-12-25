from django.contrib import admin
from . models import HospitalData, PatientData, DocterData

# Register your models here.
admin.site.register(HospitalData)
admin.site.register(DocterData)
admin.site.register(PatientData)


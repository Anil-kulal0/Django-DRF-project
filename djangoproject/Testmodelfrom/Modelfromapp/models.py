from django.db import models

# Create your models here.

class HospitalData(models.Model):
    hospital_name = models.CharField('Hospital Name',max_length=100)
    hospital_contact = models.IntegerField('Contact Number')
    hospital_address = models.TextField('Hospital Address')
    hospital_emailid = models.EmailField()
    hospital_specialization = models.CharField('Hospital Specialization',max_length=200)
    
    def __str__(self):
        return self.hospital_name

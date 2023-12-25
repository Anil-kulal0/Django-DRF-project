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
    
    
class DocterData(models.Model):
    docter_name = models.CharField('Docter Name', max_length=100)
    docter_specilization = models.CharField('Specialization', max_length=200)
    docter_doj = models.DateField('Date of Joining')
    
    def __str__(self):
        return self.docter_name
    
    
class PatientData(models.Model):
    patient_name = models.CharField('Patient Name', max_length=100)
    patient_ward = models.CharField('Patient Ward', max_length=10)
    patient_age = models.IntegerField('Patient Age')
    patient_contact = models.IntegerField('Patient Contact')
    patient_address = models.TextField('Patient Address', max_length=200)
    patient_type = models.CharField('Patient Type', max_length=5)
    patient_doa = models.DateField('Date of Addimission')
    patient_dod = models.DateField('Date of Discharge')
    patient_hospital = models.ForeignKey('HospitalData', on_delete=models.CASCADE)
    patient_docter = models.ForeignKey('DocterData', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.patient_name
        
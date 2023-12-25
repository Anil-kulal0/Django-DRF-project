from django import forms
from . models import DocterData,PatientData,HospitalData
"""
class DocterFrom(forms.Form):
    docter_name = forms.CharField(label='Docter Name', max_length=100)
    docter_specilization = forms.CharField(label='Specialization', max_length=200)
    docter_doj = forms.DateField(label='Date of Joining')
    """
    
class DocterFrom(forms.ModelForm):
    
    class Meta:
        model = DocterData 
        fields = ['docter_name','docter_specilization','docter_doj']
        
class PatientFrom(forms.ModelForm):
    
    class Meta:
        model = PatientData 
        fields = ['patient_name','patient_ward','patient_age','patient_contact','patient_address','patient_type','patient_doa','patient_dod','patient_hospital','patient_docter']


class HospitalFrom(forms.ModelForm):
    
    class Meta:
        model = HospitalData 
        fields = ['hospital_name','hospital_contact','hospital_address','hospital_emailid','hospital_specialization']

from django import forms
from.models import HospitalData 


class HospitalFrom(forms.ModelForm):
    class Meta:
        model = HospitalData
        fields = ['hospital_name','hospital_contact','hospital_address','hospital_emailid','hospital_specialization'] 
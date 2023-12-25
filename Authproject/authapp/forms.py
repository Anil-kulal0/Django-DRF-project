from django.contrib.auth.models import User

from django import forms

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")

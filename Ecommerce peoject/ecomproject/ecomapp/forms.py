from django import forms
from .models import Order, Customer
from django.contrib.auth.models import User

class checkoutForm(forms.ModelForm):
      class Meta:
            model = Order
            fields = ['orderd_by','shipping_address','mobile','email']
            
class customerregistrationForm(forms.ModelForm):
      username = forms.CharField(widget=forms.TextInput)
      password = forms.CharField(widget=forms.PasswordInput)
      email = forms.EmailField(widget=forms.EmailInput)
      
      class Meta:
            model = Customer
            fields = ['username','password','email','full_name','address']
            
      def clean_username(self):
            uname = self.cleaned_data.get('username')
            if User.objects.filter(username= uname).exists():
                  raise forms.ValidationError('customer with this usrename already exists')
            return uname
class customerloginForm(forms.Form):
      username = forms.CharField(widget=forms.TextInput)
      password = forms.CharField(widget=forms.PasswordInput)
      
            
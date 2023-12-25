from django.shortcuts import render
from.forms import HospitalFrom
from django.http import HttpResponseRedirect

# Create your views here.
def registerhospital(request):
    if request.POST:
        form = HospitalFrom(request.POST)
    
        if form.is_valid():
            #form.save()
            print('Data Save')
        
        return HttpResponseRedirect('/')
        
        
        
    form = HospitalFrom()        
    return render (request,'hospitalregister.html', {'form':form})
    

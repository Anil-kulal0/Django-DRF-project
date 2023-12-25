from django.shortcuts import render
from django.http import HttpResponseRedirect
from.forms import DocterFrom,PatientFrom
from.models import DocterData

# Create your views here.
def index(request):
    form = PatientFrom()
    return render(request,'register.html',{'form': form})

def registerdocter(request):
    if request.method == "POST":
        form = DocterFrom(request.POST)
        
        if form.is_valid():
            
            docter_name = request.POST['docter_name']
            docter_specilization = request.POST['docter_specilization']
            docter_doj = request.POST['docter_doj']            
            #INSERT DATA TO DB
            obj = DocterData(docter_name=docter_name, docter_specilization=docter_specilization, docter_doj=docter_doj)
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = DocterFrom()
        
    return render(request,'register.html',{'form': form})
        
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import UserData

# Create your views here.
def index(request):
    #userdata = [{'fullname':'anil kulal', 'emailid':'anilkulal@gmail.com', 'contact':'4567845674', 'address':'pune,maharastra', 'username':'anil', 'password':'anil1010' },
    #{'fullname':'manohar kulal', 'emailid':'manoharkulal@gmail.com', 'contact':'4567845674', 'address':'mumbai,maharastra', 'username':'manohar', 'password':'anil1010' },
    #{'fullname':'kartik dombale', 'emailid':'kartikdombale@gmail.com', 'contact':'4567845674', 'address':'jath,maharastra', 'username':'kartik', 'password':'anil1010' },
    #]
    
    alldata = UserData.objects.all()
    return render(request,'index.html',context={'data':alldata})



def register(request):
    return render(request,'register.html')

def registeruser(request):
    if request.POST:
        fullname = request.POST['fullname']
        emailid = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        username = request.POST['username']
        inputpassword = request.POST['inputpassword']
        confirmpassword = request.POST['confirmpassword']
        
        if inputpassword==confirmpassword:
            obj = UserData(fullname=fullname,emailid=emailid, contact=contact, address=address,username=username, password=inputpassword)
            obj.save()
            
            alldata = UserData.objects.all()
        
            return render(request,'index.html',context={'data':alldata, 'flag':'success'})
        else:
            return render(request,'register.html',{'flag':'invalid'})

    return render(request,'register.html')

def deleteme(request,id):
    obj = UserData.objects.get(id=id)
    obj.delete()
        
    alldata = UserData.objects.all()
        
    return render(request,'index.html',context={'data':alldata})
    
    
def editme(request, id):
    if request.POST:
        fullname = request.POST['fullname']
        emailid = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        
        obj = UserData.objects.get(id=id)
        obj.fullname = fullname
        obj.emailid = emailid 
        obj.contact = contact
        obj.address = address
        obj.save()
        
        alldata = UserData.objects.all()
        
        return render(request,'index.html',context={'data':alldata})
    obj = UserData.objects.get(id=id)
    #print(obj.username)
    #obj.delete()
    
    alldata = UserData.objects.all()
    return render(request,'edit.html',context={'data':obj})
    
    
    

def searchdata(request):
    
    if request.POST:
        if 'fullname' in request.POST:
            searchtext = request.POST['searchtext']
            print(request.POST['fullname'])
            fullname=True
            filteredobj = UserData.objects.filter(fullname__contains=searchtext)
    
            return render(request,'index.html',context={'data' :filteredobj})
    
    alldata = UserData.objects.all()
    return render(request,'index.html',context={'data':alldata})

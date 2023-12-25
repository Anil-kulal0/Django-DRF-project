from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    # return HttpResponse('hello')
    
    data ={'name':'Anil'}
    return render (request,'index.html',data)
def aboutus (request):
    return render (request,'about.html')
def registerme(request):
    dic={}
    if request.POST['emailid']:
        dic['email']=request.POST['emailid']
    if request.POST['address']:
        dic['address']=request.POST['address']
    print(dic)
    return HttpResponse('get post')
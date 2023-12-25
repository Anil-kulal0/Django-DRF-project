from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    
    a=12
    b=23
    c=a+b
    res=f'Addition {a} and {b} = {c}'
    return HttpResponse (res)

def index(request):
    pagetitle='homepage'
    content='this my index page'
    
    return render (request,'index.html',{'pagetitle':pagetitle,'content':content}) 

def about(request):
    pagetitle='aboutpage'
    content='this is about page'
    return render (request,'about.html',{'pagetitle':pagetitle,'content':content}) 

def contact(request):
    pagetitle='contactpage'
    content='this is contact page'
    contact = ['anil',9284656081],['kartik',2158309832578]
    return render (request,'contact.html',{'pagetitle':pagetitle,'content':content,'contact':contact}) 

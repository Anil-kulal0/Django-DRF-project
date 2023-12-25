from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all(request):
    a=20
    b=40
    c=a+b
    res = f'Addition {a} and {b} = {c}'
    return HttpResponse(res)

def index(request):
    pagetitle = 'HomePage'
    content = 'THIS IS INDEX PAGE'
    return render(request,'index.html',{'pagetitle': pagetitle,'content':content})

def about(request):
    pagetitle = 'AboutPage'
    content = 'THIS IS ABOUT PAGE' 
    return render(request,'about.html',{'pagetitle': pagetitle,'content':content})

def contact(request):
    pagetitle = 'ContactPage'
    content = 'THIS IS CONTACT PAGE'
    
    contact_det = [[1,'Anil',9284656081],
                   [2,'Manohar',8928138644],
                   [3,'Tushar',8411928569],
                   [4,'kartik',9284656081],
                   [5,'valmik',9594638201]]
    return render(request,'contact.html',{'pagetitle': pagetitle,'content':content,'contactdet':contact_det})

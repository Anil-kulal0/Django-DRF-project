from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def myfunc(request):
    a=10
    b=20
    c=a+b
    res= f'addition of {a} and {b}={c}'
    return HttpResponse(res)
def index(request):
    pagetitle = 'Homepage'
    content = 'This is my index page'
    return render(request,'index.html',{'pagetitle':pagetitle,'content':content})
def about(request):
    pagetitle = 'Aboutpage'
    content = 'This is my about page'
    return render(request,'about.html',{'pagetitle':pagetitle,'content':content})
def contact(request):
    pagetitle = 'Contactpage'
    content = 'This is my contact page'
    
    contact_det = [['anil',9865564681], ['manohar',89729865976], ['kartik',92157985587]]    
    
    return render(request,'contact.html',{'pagetitle':pagetitle,'content':content,'contactdet':contact_det })

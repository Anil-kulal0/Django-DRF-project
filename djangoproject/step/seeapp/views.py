from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cal(request):
    return HttpResponse("I am anil how are you")
def all(request):
    return render(request,'call.html')
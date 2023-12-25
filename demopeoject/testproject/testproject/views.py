from django.http import HttpResponse
from django.shortcuts import render
def home (request):
    return HttpResponse('<b>this is my first project django</b>')

def index (request):
    return render (request,'index.html')
def home (request):
    return render(request,'home.html')
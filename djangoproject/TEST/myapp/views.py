from django.shortcuts import render

# Create your views here.


def f1(request):
    return render(request,'home.html')
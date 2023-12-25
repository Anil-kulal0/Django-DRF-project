from django.shortcuts import render
from .forms import UserForms
from django.http import HttpResponseRedirect
# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method =='POST':
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/signup/')
    form = UserForms()
    return render(request, 'register.html', {'form':form})


    
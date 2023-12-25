from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import UserData

# Create your views here.

def check_active_session(request):
    return request.session.get('username', False)

def logout(request):
    del request.session['userid']
    del request.session['email']
    del request.session['username']
    return HttpResponseRedirect('/')

def login(request):
    return render(request, 'login.html')

def logincheck(request):
    if request.POST:
        if 'username' in request.POST:
            username = request.POST['username']
            status=True
        else:
            status=False
        if 'passwd' in request.POST:
            passwd = request.POST['passwd']
            status=True
        else:
            status=False

        if status:
            obj = UserData.objects.filter(username=username, password=passwd)
            if obj:
                request.session['userid'] = obj[0].id
                request.session['email'] = obj[0].email
                request.session['username'] = username

                return HttpResponseRedirect('/home/')

    return render(request, 'login.html')

"""
def index(request):
    alldata = UserData.objects.all()
    return render(request, 'index.html', context={'data': alldata})
"""
def index(request):
    if request.session.get('username', False):
        alldata = UserData.objects.all()
        return render(request, 'index.html', context={'data': alldata})
    else:
        return HttpResponseRedirect('/')

def register(request):
    return render(request, 'register.html')

def registeruser(request):
    if request.POST:
        fullname = request.POST['fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        username = request.POST['username']
        inputpassword = request.POST['inputpassword']
        confirmpassword = request.POST['confirmpassword']

        print(fullname, email, contact, address, username, inputpassword, confirmpassword)

        if inputpassword==confirmpassword :
            obj = UserData(fullname=fullname, email=email, contact=contact, address=address, username=username, password=inputpassword)
            obj.save()

            alldata = UserData.objects.all()
            return render(request, 'index.html', context={'data': alldata, 'flag':'success'})
        else:
            return render(request, 'register.html', {'flag':'invalid'})

    return render(request, 'register.html')

def deleteme(request, id):
    obj = UserData.objects.get(id=id)
    obj.delete()

    alldata = UserData.objects.all()
    return render(request, 'index.html', context={'data': alldata, 'flag':'success'})

def editme(request, id):
    if request.POST:
        fullname = request.POST['fullname']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']

        obj = UserData.objects.get(id=id)
        obj.fullname = fullname
        obj.email = email
        obj.contact = contact
        obj.address = address

        obj.save()

        alldata = UserData.objects.all()
        return render(request, 'index.html', context={'data': alldata})


    obj = UserData.objects.get(id=id)

    return render(request, 'edit.html', context={'data': obj})


def searchdata(request):

    if request.POST:
        if 'fullname' in request.POST:
            searchtext = request.POST['searchtext']
            print(request.POST['fullname'])
            fullname=True
            
            filteredobjs = UserData.objects.filter(fullname__contains=searchtext)
   
            return render(request, 'index.html', context={'data': filteredobjs})
    
    alldata = UserData.objects.all()
    return render(request, 'index.html', context={'data': alldata})
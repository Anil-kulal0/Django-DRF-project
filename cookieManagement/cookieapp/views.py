from django.shortcuts import render


# Create your views here.
def visitcounter(request):
    #print(dir(request.COOKIES),type(request.COOKIES), request.COOKIES)
    if request.COOKIES:
        count = int(request.COOKIES.get('count',0))
        count += 1
        response = render (request,'cookieapp/index.html', {'count':count})
        response.set_cookie('count', count)

        return response


def visitcounterpersistent(request):
    #print(dir(request.COOKIES),type(request.COOKIES), request.COOKIES)
    if request.COOKIES:
        count = int(request.COOKIES.get('countp',0))
        count += 1
        response = render (request,'cookieapp/index.html', {'count':count})
        response.set_cookie('countp', count, max_age=20)

        return response

# def registeritem(request):
#     if request.POST:
#         itemname = request.POST['itemname']
#         qty = request.POST['qty']
#         if request.COOKIES:
#             response = render (request, 'cookieapp/showitems.html')
#             response.set_cookie('itemname', itemname)
#             response.set_cookie('qty', qty)
#             return response
#     return render (request, 'cookieapp/registeritems.html')

def registeritem(request):
    if request.POST:
        itemname = request.POST['itemname']
        qty = request.POST['qty']
        itemdict = request.session.get('itemdict',{})
        itemdict[itemname] = qty
        request.session['itemdict'] = itemdict
    return render (request, 'cookieapp/registeritems.html')

def showitems(request):
    return render(request, 'cookieapp/showitem.html')
    

def page1(request):
     return render (request, 'cookieapp/page1.html')
    
    
def page2(request):
    name1 = request.POST['name1']
    if request.COOKIES: 
        response = render(request, 'cookieapp/page2.html') 
        response.set_cookie('name1', name1)
        return response
    
def page3(request):
    name2 = request.POST['name2']
    if request.COOKIES: 
        response = render(request, 'cookieapp/page3.html') 
        response.set_cookie('name2', name2)
        return response
    
def showdata(request):
    name3 = request.POST['name3']
    if request.COOKIES: 
        li = [ele for ele in request.COOKIES.values()]
        li += [name3]
        response = render(request, 'cookieapp/showdata.html', {'data':li[1:]}) 
        response.set_cookie('name3', name3)
        return response
    
       
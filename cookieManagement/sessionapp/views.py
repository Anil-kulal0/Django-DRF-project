from django.shortcuts import render

# Create your views here.

def visitcounter(request):
    # if 'count' in request.session:
        count = request.session.get('count', 0)
        count += 1
        request.session['count'] = count
        request.session.set_expiry(20)
        
        
        # print(request.session.get_expiry_age())
        # print(request.session.get_expiry_date())
        
        
        data = {'count':count, 'expiry_age':request.session.get_expiry_age(), 'expiry_date':request.session.get_expiry_date()}
    
        return render (request,'sessionapp/index.html',   data)
    
def restart(request):
    # request.session.clear()
    # request.session.flush()
    del request.session['count']    
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    
    return render (request,'sessionapp/index.html',  {'count':count})
    
def showsessionval(request):
    return render(request,'session/showsessionvalue.html',{'sessiondata': request.session})
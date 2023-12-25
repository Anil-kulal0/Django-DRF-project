from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import FileData
# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = FileData(title=request.POST['title'], filename=request.FILES['filename'])
            instance.save()
            return HttpResponseRedirect('/uploadfile/')
    else:
        form = UploadFileForm()
        
    return render(request, 'uploadfile.html', {'form':form})

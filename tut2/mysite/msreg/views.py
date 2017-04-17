from django.http import HttpResponse
from django.template import loader
# Create your views here.



def index(request):
	return HttpResponse('Okay, we will just live with bloody templates for now')

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file. Needs to be written
from handler import handle_uploaded_file

def results(request):
    return HttpResponse('Youve made it')

def upload_file(request):
    #template = loader.get_template('polls/results.html')
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'msreg/results.html', {'form': form})

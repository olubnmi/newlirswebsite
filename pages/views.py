from django.shortcuts import render
from django.http import HttpResponse
from .models import Popup
# Create your views here.

def index(request) :
    popups = Popup.objects.all()
    context = {
        'popups' : popups
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')
def faq(request):
    return render(request,'pages/faq.html')
def contact(request):
    return render(request,'pages/contact.html')
def ec(request):
    return render(request,'pages/ec.html')
def da(request):
    return render(request,'pages/da.html')
def dbs(request):
    return render(request,'pages/dbs.html')
def dhr(request):
    return render(request,'pages/dhr.html')
def dissd(request):
    return render(request,'pages/dissd.html')
def dls(request):
    return render(request,'pages/dls.html')
def dnga(request):
    return render(request,'pages/dnga.html')
def dpit(request):
    return render(request,'pages/dpit.html')
def dta(request):
    return render(request,'pages/dta.html')
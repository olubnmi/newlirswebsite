from django.shortcuts import render
from django.http import HttpResponse
from .models import Taxlegislation

# Create your views here.
def index(request) :
    taxlegislations = Taxlegislation.objects.all()
    context = {
        'taxlegislations' : taxlegislations
    }
    return render(request,'taxlegislations/taxlegislations.html',context)
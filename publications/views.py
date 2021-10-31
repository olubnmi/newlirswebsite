from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Publication

# Create your views here.
def index(request) :
    publications = Publication.objects.all().order_by('-id')
    paginator = Paginator(publications, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'publications' : page_obj
    }
    return render(request,'publications/publications.html',context)
from django.shortcuts import render
from .models import *

def main_page(request):
    companies=Company.objects.all()
    rates=Rate.objects.all()
    return render(request,'handbook/main_page.html',{'companies':companies,'rates':rates})

def catalog(request):
    return render(request,'handbook/catalog_of_companies.html',{})
# Create your views here.

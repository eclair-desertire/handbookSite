from django.shortcuts import render, get_object_or_404
from .models import *

def main_page(request):
    return render(request,'handbook/main_page.html',{})

def ishop(request):
    ishops=Company.objects.filter(comapny_category='Internet Shop')
    return render(request,'handbook/ishop.html',{'ishops':ishops})

def smarket(request):
    smaerkets=Company.objects.filter(comapny_category='SuperMarket')
    return render(request,'handbook/smarket.html',{'smarkets':smaerkets})

def shopping(request):
    shops=Company.objects.filter(comapny_category='Shopping center')
    return render(request,'handbook/shopping.html',{'shops':shops})

def fshop(request):
    fshops=Company.objects.filter(comapny_category='Furniture Shop')
    return render(request,'handbook/fshop.html',{'fshops':fshops})

def icompany(request):
    icomps=Company.objects.filter(comapny_category='IT Company')
    return render(request,'handbook/icompany.html',{'icomps':icomps})

def edu(request):
    edus=Company.objects.filter(comapny_category='Educational Center')
    return render(request,'handbook/edu.html',{'edus':edus})

def company_detail(request,pk):
    company=get_object_or_404(Company,pk=pk)
    rate=Rate.objects.all()
    return render(request,'handbook/details.html',{'company':company,'rate':rate})
# Create your views here.

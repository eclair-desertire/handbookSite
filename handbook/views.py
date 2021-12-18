from django.shortcuts import render
from .models import *

def main_page(request):
    return render(request,'handbook/main_page.html',{})

def ishop(request):
    return render(request,'handbook/ishop.html',{})

def smarket(request):
    return render(request,'handbook/smarket.html',{})

def shopping(request):
    return render(request,'handbook/shopping.html',{})

def fshop(request):
    return render(request,'handbook/fshop.html',{})

def icompany(request):
    return render(request,'handbook/icompany.html',{})

def edu(request):
    return render(request,'handbook/edu.html',{})
# Create your views here.

from django.shortcuts import render
from .models import *
def main_page(request):
    companies=Company.objects.all()
    rates=Rate.objects.all()
    return render(request,'handbook/main_page.html',{'companies':companies,'rates':rates})

# Create your views here.

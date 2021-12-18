from django.shortcuts import render

def main_page(request):
    return render(request,'handbook/main_page.html',{})

# Create your views here.

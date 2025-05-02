from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products': products})

def aboutme(request):
    return render(request, 'aboutme.html')
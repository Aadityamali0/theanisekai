from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

def anime(request):
    return render(request, 'anime/index.html')

def product(request):
    products = Product.objects.all()
    params = {'product' : products}
    return render(request, 'anime/product.html', params)
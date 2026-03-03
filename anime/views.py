from django.shortcuts import render
from math import ceil
from . models import Product

def index(request):
    return render(request, 'anime/index.html')

def product(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//3 + ceil((n/3) - (n//3))
    params = {'anime' : products, 'no_of_slides' : nSlides, 'range' : range(1, nSlides)  }
    return render(request, 'anime/anime.html', params)

def demo(request):
    return render(request, 'anime/demo.html')
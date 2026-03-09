from django.shortcuts import render
from math import ceil
from .models import Product

def index(request):
    allProds = []
    catprods = Product.objects.values('category')

    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n/4)
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'anime/index.html', params)
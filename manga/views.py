from django.shortcuts import render
from django.http import HttpResponse

def manga(request):
    return render(request, 'manga/index.html')
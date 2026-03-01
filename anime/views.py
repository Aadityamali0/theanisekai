from django.shortcuts import render
from django.http import HttpResponse

def anime(request):
    return render(request, 'anime/index.html')

def about(request):
    return HttpResponse("we are at about us")

def contact(request):
    return HttpResponse("we are at contact us")

def tracker(request):
    return HttpResponse("we are at tracking")
def search(request):
    return HttpResponse("we are at search")
def product(request):
    return HttpResponse("we are at productview us")
def checkout(request):
    return HttpResponse("we are at checkout")
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "europa/index.html")

def portugal(request):
    return render(request, "europa/portugal.html")

def espanha(request):
    return render(request, "europa/espanha.html")
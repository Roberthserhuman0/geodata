from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "sulamerica/inicio.html")

def brasil(request):
    return render(request, "sulamerica/brasil.html")

def argentina(request):
    return render(request, "sulamerica/argentina.html")

def uruguai(request):
    return render(request, "sulamerica/uruguai.html")

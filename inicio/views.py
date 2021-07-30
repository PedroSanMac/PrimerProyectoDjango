from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def primeraView(request, *args, **kwargs):
    return render(request, "primera.html", {})

def segundaView(request, *args, **kwargs):
    return render(request, "segunda.html", {})
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def menu(request):
    return render(request,"menu.html",{})

def acercaDe(request):
    return render(request,"acercaDe.html",{})

def contacto(request):
    return render(request,"contacto.html",{})

from django.http import HttpResponse
from django.shortcuts import render

def myHomeView(request, *args, **kwargs):
    """Vista principal que será migrada a template en el siguiente commit"""
    print(request.user)  # Debug: ver usuario en consola
    return render(request, "home.html",{})  # Preparada para template

def anotherView(request):
    """Vista secundaria (se actualizará luego)"""
    return HttpResponse('<h1>Sólo otra página</h1>')
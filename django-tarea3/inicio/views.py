from django.http import HttpResponse
from django.shortcuts import render

def myHomeView(request, *args, **kwargs):
    print(request.user)  # Debug: ver usuario en consola
    myContext = {
        'myText': 'Esto es sobre nosotros',
        'myNumber': 123,
        'myList': [313, 44544, 55, 89.90, 324],
        }
    return render(request, "home.html", myContext)  # Preparada para template

def anotherView(request):
    """Vista secundaria (se actualizará luego)"""
    return HttpResponse('<h1>Sólo otra página</h1>')
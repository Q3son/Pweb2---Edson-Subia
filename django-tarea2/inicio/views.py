from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h1>Hola Mundo desde Django</h1>')

def anotherView(request):
    return HttpResponse('<h1>Sólo otra página</h1>')
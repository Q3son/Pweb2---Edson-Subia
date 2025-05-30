from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(*args, **kwargs):
    return HttpResponse('<h1>Hola Mundo desde Django</h1>')
# personas/views.py
from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Bienvenido a mi app de contactos!")
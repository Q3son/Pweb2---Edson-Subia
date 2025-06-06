# personas/views.py
from django.shortcuts import render
from .models import Persona 
from django.http import HttpResponse

def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    obj2 = Persona.objects.get(id = 2)
    context = {
        'nombre': obj.nombres,
        'edad': obj.edad,
        'objeto2': obj2, 
    }
    return render (request, 'personas/test.html', context)
def inicio(request):
    return HttpResponse("¡Bienvenido a mi app de contactos!")
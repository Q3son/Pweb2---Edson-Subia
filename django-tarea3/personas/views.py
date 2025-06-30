# personas/views.py
from django.shortcuts import render
from .models import Persona 
from .forms import PersonaForm
from django.http import HttpResponse

def personaTestView(request):
    obj = Persona.objects.get(id = 1)
    obj2 = Persona.objects.get(id = 2)
    context = {
        'nombre': obj.nombre,
        'edad': obj.edad, 
        'objeto2': obj2,
    }
    return render (request, 'personas/descripcion.html', context)
def personaCreateView(request):
    print(request)
    if request.method == 'POST':
        nombre = request.POST.get('q')
        print(nombre)
    context = {}
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})

def inicio(request):
    return HttpResponse("¡Bienvenido a mi app de contactos!")
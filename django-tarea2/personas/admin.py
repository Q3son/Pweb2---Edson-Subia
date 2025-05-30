# personas/admin.py
from django.contrib import admin
from .models import Persona  # Cambiar Contacto por Persona

@admin.register(Persona)  # Actualizar aquí también
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'edad')
    search_fields = ('nombre', 'apellidos')
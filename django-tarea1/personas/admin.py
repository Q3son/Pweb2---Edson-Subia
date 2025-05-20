from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro', 'activo')
    search_fields = ('nombre', 'email')
    list_filter = ('activo', 'fecha_registro')
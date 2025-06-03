from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import DestinosTuristicos

@admin.register(DestinosTuristicos)
class DestinosAdmin(admin.ModelAdmin):
    list_display = ('nombreCiudad', 'precioTour', 'ofertaTour', 'created_by')
    list_filter = ('ofertaTour',)
    search_fields = ('nombreCiudad', 'descripcionCiudad')
    prepopulated_fields = {'slug': ('nombreCiudad',)}  # Si agregas campo slug

admin.site.site_header = "Administración de Perú Tourism"
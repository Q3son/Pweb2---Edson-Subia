from django.contrib import admin
from django.utils import timezone  # ¡Importación faltante!
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    def formatted_fecha(self, obj):
        return timezone.localtime(obj.fecha_registro).strftime('%d/%m/%Y %H:%M')
    formatted_fecha.short_description = 'Fecha registro'
    formatted_fecha.admin_order_field = 'fecha_registro'
    
    # Usa EL MISMO nombre en list_display (o usa el método personalizado)
    ordering = ('-fecha_registro',)
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro', 'formatted_fecha')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_registro', 'activo')
    date_hierarchy = 'fecha_registro'
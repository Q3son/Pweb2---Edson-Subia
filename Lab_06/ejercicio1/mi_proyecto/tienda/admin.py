from django.contrib import admin
from .models import Producto, Venta

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'precio', 'stock')
    search_fields = ('codigo', 'nombre')
    list_filter = ('precio',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha', 'cliente')
    list_filter = ('fecha', 'producto')
    date_hierarchy = 'fecha'
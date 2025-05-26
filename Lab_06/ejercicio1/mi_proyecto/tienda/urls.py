from django.urls import path
from .views import (
    home, 
    ListaProductosView, 
    CrearVentaView, 
    lista_ventas,
    detalle_producto
)

urlpatterns = [
    path('', home, name='home'),
    path('productos/', ListaProductosView.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('ventas/crear/', CrearVentaView.as_view(), name='crear_venta'),
    path('ventas/', lista_ventas, name='lista_ventas'),
]
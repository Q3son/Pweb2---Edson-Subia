from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Producto, Venta
from .forms import VentaForm

def home(request):
    return render(request, 'tienda/home.html')

class ListaProductosView(ListView):
    model = Producto
    template_name = 'tienda/lista_productos.html'
    context_object_name = 'productos'
    paginate_by = 10

class CrearVentaView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'tienda/crear_venta.html'
    success_url = '/ventas/'

def lista_ventas(request):
    ventas = Venta.objects.select_related('producto').order_by('-fecha')
    return render(request, 'tienda/lista_ventas.html', {'ventas': ventas})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    ventas = Venta.objects.filter(producto=producto).order_by('-fecha')
    return render(request, 'tienda/detalle_producto.html', {
        'producto': producto,
        'ventas': ventas
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import DestinosTuristicos
from .forms import DestinoForm

def home(request):
    """Vista principal que muestra destinos en oferta"""
    destinos = DestinosTuristicos.objects.filter(ofertaTour=True).order_by('?')[:3]  # Aleatorios
    return render(request, 'home.html', {'destinos': destinos})

@login_required
def add_destino(request):
    """Vista para añadir nuevos destinos turísticos"""
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            destino = form.save(commit=False)
            destino.created_by = request.user
            destino.save()
            messages.success(request, 'Destino creado exitosamente!')
            return redirect('list_destinos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = DestinoForm()
    
    context = {
        'form': form,
        'title': 'Agregar Nuevo Destino'
    }
    return render(request, 'destinos/add_destino.html', context)

@login_required
def list_destinos(request):
    """Lista todos los destinos con paginación"""
    destinos_list = DestinosTuristicos.objects.all().order_by('nombreCiudad')
    
    # Paginación (6 items por página)
    paginator = Paginator(destinos_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'title': 'Todos los Destinos Turísticos'
    }
    return render(request, 'destinos/list_destinos.html', context)

@login_required
def edit_destino(request, id):
    """Edita un destino existente"""
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    
    # Verificar que el usuario sea el creador o superusuario
    if request.user != destino.created_by and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para editar este destino.')
        return redirect('list_destinos')
    
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destino actualizado correctamente!')
            return redirect('list_destinos')
    else:
        form = DestinoForm(instance=destino)
    
    context = {
        'form': form,
        'destino': destino,
        'title': f'Editar {destino.nombreCiudad}'
    }
    return render(request, 'destinos/edit_destino.html', context)

@login_required
def delete_destino(request, id):
    """Elimina un destino"""
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    
    # Verificar permisos
    if request.user != destino.created_by and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para eliminar este destino.')
        return redirect('list_destinos')
    
    if request.method == 'POST':
        destino.delete()
        messages.success(request, 'Destino eliminado correctamente.')
        return redirect('list_destinos')
    
    context = {
        'destino': destino,
        'title': f'Eliminar {destino.nombreCiudad}'
    }
    return render(request, 'destinos/delete_destino.html', context)

def detail_destino(request, id):
    """Muestra los detalles de un destino específico"""
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    
    # Incrementar contador de vistas (opcional)
    destino.views = destino.views + 1 if hasattr(destino, 'views') else 1
    destino.save()
    
    context = {
        'destino': destino,
        'title': destino.nombreCiudad
    }
    return render(request, 'destinos/detail_destino.html', context)
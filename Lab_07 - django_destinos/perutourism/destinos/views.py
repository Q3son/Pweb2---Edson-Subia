from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import DestinosTuristicos
from .forms import DestinoForm

# Importaciones para autenticación
from django.contrib.auth.forms import UserCreationForm # <--- IMPORTANTE
from django.contrib.auth.views import LoginView # Para la vista de login
from django.contrib.auth import logout # Para la vista de logout

def home(request):
    """Vista principal que muestra destinos en oferta"""
    destinos = DestinosTuristicos.objects.filter(ofertaTour=True).order_by('?')[:3]
    return render(request, 'home.html', {'destinos': destinos})

def register_view(request):
    """Vista para el registro de nuevos usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login') # Redirige a la página de login
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario de registro.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required # Asegura que solo usuarios logueados puedan desloguearse
def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('home') # O a donde quieras redirigir después del logout

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
            return redirect('destinos:list_destinos')
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

    if request.user != destino.created_by and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para editar este destino.')
        return redirect('destinos:list_destinos')

    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destino actualizado correctamente!')
            return redirect('destinos:list_destinos')
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

    if request.user != destino.created_by and not request.user.is_superuser:
        messages.error(request, 'No tienes permiso para eliminar este destino.')
        return redirect('destinos:list_destinos')

    if request.method == 'POST':
        destino.delete()
        messages.success(request, 'Destino eliminado correctamente.')
        return redirect('destinos:list_destinos')

    context = {
        'destino': destino,
        'title': f'Eliminar {destino.nombreCiudad}'
    }
    return render(request, 'destinos/delete_destino.html', context)

def detail_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    return render(request, 'destinos/detail_destino.html', {'destino': destino})
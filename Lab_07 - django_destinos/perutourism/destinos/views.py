from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DestinosTuristicos
from .forms import DestinoForm

def home(request):
    destinos = DestinosTuristicos.objects.filter(ofertaTour=True)[:3]
    return render(request, 'home.html', {'destinos': destinos})

@login_required
def add_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            destino = form.save(commit=False)
            destino.created_by = request.user
            destino.save()
            return redirect('list_destinos')
    else:
        form = DestinoForm()
    return render(request, 'add_destino.html', {'form': form})

@login_required
def list_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'list_destinos.html', {'destinos': destinos})

@login_required
def edit_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('list_destinos')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'edit_destino.html', {'form': form})

@login_required
def delete_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('list_destinos')
    return render(request, 'delete_destino.html', {'destino': destino})

def detail_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, pk=id)
    return render(request, 'detail_destino.html', {'destino': destino})
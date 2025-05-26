from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView
)
from django.urls import reverse_lazy
from django.contrib import messages  # Importar messages
from .models import Alumno, Curso, NotaAlumnoPorCurso
from .forms import AlumnoForm, CursoForm, NotaForm

def home(request):
    """Vista para la página de inicio"""
    return render(request, 'educacion/home.html')
class AlumnoListView(ListView):
    model = Alumno
    template_name = 'educacion/alumno_list.html'
    context_object_name = 'alumnos'
    paginate_by = 20

class AlumnoCreateView(CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'educacion/alumno_form.html'
    success_url = reverse_lazy('alumno_list')

    def form_valid(self, form):
        messages.success(self.request, f'Alumno {form.instance.nombre} {form.instance.apellido} creado exitosamente!')
        return super().form_valid(form)

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'educacion/alumno_form.html'
    success_url = reverse_lazy('alumno_list')

    def form_valid(self, form):
        messages.success(self.request, f'Datos de {form.instance.nombre} {form.instance.apellido} actualizados correctamente!')
        return super().form_valid(form)

class CursoListView(ListView):
    model = Curso
    template_name = 'educacion/curso_list.html'
    context_object_name = 'cursos'

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'educacion/curso_form.html'
    success_url = reverse_lazy('curso_list')

    def form_valid(self, form):
        messages.success(self.request, f'Curso {form.instance.nombre} creado exitosamente!')
        return super().form_valid(form)

class NotaListView(ListView):
    model = NotaAlumnoPorCurso
    template_name = 'educacion/nota_list.html'
    context_object_name = 'notas'
    
    def get_queryset(self):
        return super().get_queryset().select_related('alumno', 'curso')

class NotaCreateView(CreateView):
    model = NotaAlumnoPorCurso
    form_class = NotaForm
    template_name = 'educacion/nota_form.html'
    success_url = reverse_lazy('nota_list')

    def form_valid(self, form):
        messages.success(
            self.request,
            f'Nota {form.instance.nota} registrada para {form.instance.alumno} en {form.instance.curso}'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al registrar la nota. Verifique los datos.')
        return super().form_invalid(form)

class ReporteNotasView(DetailView):
    model = Alumno
    template_name = 'educacion/reporte_notas.html'
    context_object_name = 'alumno'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notas'] = NotaAlumnoPorCurso.objects.filter(
            alumno=self.object
        ).select_related('curso')
        return context
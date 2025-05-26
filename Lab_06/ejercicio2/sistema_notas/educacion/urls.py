from django.urls import path
from .views import (
    AlumnoListView, AlumnoCreateView, AlumnoUpdateView,
    CursoListView, CursoCreateView,
    NotaListView, NotaCreateView,
    ReporteNotasView
)

urlpatterns = [
    # Alumnos
    path('alumnos/', AlumnoListView.as_view(), name='alumno_list'),
    path('alumnos/nuevo/', AlumnoCreateView.as_view(), name='alumno_create'),
    path('alumnos/editar/<int:pk>/', AlumnoUpdateView.as_view(), name='alumno_update'),
    path('alumnos/reporte/<int:pk>/', ReporteNotasView.as_view(), name='alumno_reporte'),
    
    # Cursos
    path('cursos/', CursoListView.as_view(), name='curso_list'),
    path('cursos/nuevo/', CursoCreateView.as_view(), name='curso_create'),
    
    # Notas
    path('notas/', NotaListView.as_view(), name='nota_list'),
    path('notas/nueva/', NotaCreateView.as_view(), name='nota_create'),
]
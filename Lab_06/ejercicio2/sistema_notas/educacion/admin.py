from django.contrib import admin
from .models import Alumno, Curso, NotaAlumnoPorCurso

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'apellido', 'nombre', 'email')
    search_fields = ('dni', 'apellido', 'nombre')
    list_filter = ('apellido',)
    ordering = ('apellido', 'nombre')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos', 'profesor')
    search_fields = ('codigo', 'nombre', 'profesor')
    list_filter = ('creditos',)

@admin.register(NotaAlumnoPorCurso)
class NotaAlumnoPorCursoAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'nota', 'fecha_evaluacion')
    search_fields = ('alumno__apellido', 'alumno__nombre', 'curso__nombre')
    list_filter = ('curso', 'fecha_evaluacion')
    raw_id_fields = ('alumno', 'curso')
    date_hierarchy = 'fecha_evaluacion'

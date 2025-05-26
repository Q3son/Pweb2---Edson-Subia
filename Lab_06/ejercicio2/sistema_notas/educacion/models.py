from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Alumno(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    class Meta:
        ordering = ['apellido', 'nombre']

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.PositiveSmallIntegerField()
    profesor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class NotaAlumnoPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )
    fecha_evaluacion = models.DateField()
    observaciones = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['alumno', 'curso']
        verbose_name = 'Nota del alumno por curso'
        verbose_name_plural = 'Notas de alumnos por cursos'
    
    def __str__(self):
        return f"{self.alumno} - {self.curso}: {self.nota}"
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()#Max digits 3
    donador = models.BooleanField()
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
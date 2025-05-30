from django.db import models

# Create your models here.
class Contacto(models.Model):
    # Creación de campos básicos para un sistema de contactos
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['nombre']  # Ordenar por nombre alfabéticamente

    def __str__(self):
        return self.nombre  # Representación legible en el admin

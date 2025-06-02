from django.db import models

class DestinoTuristico(models.Model):  # ¡Nombre más descriptivo!
    nombreCiudad = models.CharField(
        max_length=100,
        verbose_name="Nombre de la Ciudad",
        help_text="Ej: Machu Picchu, Lima, Arequipa"
    )
    
    imagenCiudad = models.ImageField(
        upload_to='destinos_peru',
        verbose_name="Imagen del Destino",
        help_text="Sube una foto representativa"
    )
    
    descripcionCiudad = models.TextField(
        verbose_name="Descripción",
        help_text="Detalles históricos, culturales o turísticos"
    )
    
    precioTour = models.IntegerField(
        verbose_name="Precio del Tour (S/)",
        help_text="Precio en soles peruanos"
    )
    
    ofertaTour = models.BooleanField(
        default=False,
        verbose_name="¿En oferta?",
        help_text="Marcar si está en promoción"
    )

    def __str__(self):
        return f"{self.nombreCiudad} - S/ {self.precioTour}"

    class Meta:
        verbose_name = "Destino Turístico"
        verbose_name_plural = "Destinos Turísticos"
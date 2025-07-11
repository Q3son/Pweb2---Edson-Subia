from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)  
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to='destinos/')
    precioTour = models.DecimalField(max_digits=8, decimal_places=2)
    ofertaTour = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0, verbose_name="Vistas")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombreCiudad
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombreCiudad)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('detail_destino', args=[str(self.slug)])    
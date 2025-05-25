from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Nuevo campo agregado
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Nuevo campo
    
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.CharField(max_length=100, blank=True)  # Nuevo campo
    
    def __str__(self):
        return f"Venta de {self.cantidad} unidades de {self.producto.nombre}"
    
    def save(self, *args, **kwargs):
        # Validar stock disponible antes de guardar
        if self.cantidad > self.producto.stock:
            raise ValueError("No hay suficiente stock disponible")
        super().save(*args, **kwargs)
from django import forms
from .models import Venta, Producto

class VentaForm(forms.ModelForm):
    codigo_producto = forms.CharField(max_length=100, label="Código del Producto")
    cliente = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = Venta
        fields = ['codigo_producto', 'cantidad', 'cliente']
    
    def clean_codigo_producto(self):
        codigo = self.cleaned_data.get('codigo_producto')
        try:
            producto = Producto.objects.get(codigo=codigo)
            if producto.stock <= 0:
                raise forms.ValidationError("El producto no tiene stock disponible")
            return codigo
        except Producto.DoesNotExist:
            raise forms.ValidationError("El producto con este código no existe.")
    
    def save(self, commit=True):
        codigo = self.cleaned_data.get('codigo_producto')
        producto = Producto.objects.get(codigo=codigo)
        venta = super().save(commit=False)
        venta.producto = producto
        
        if commit:
            venta.save()
            # Actualizar stock del producto
            producto.stock -= venta.cantidad
            producto.save()
        
        return venta
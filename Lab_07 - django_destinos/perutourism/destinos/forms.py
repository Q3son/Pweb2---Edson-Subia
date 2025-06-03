from django import forms
from .models import DestinosTuristicos

class DestinoForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = ['nombreCiudad', 'descripcionCiudad', 'imagenCiudad', 
                 'precioTour', 'ofertaTour']
        widgets = {
            'descripcionCiudad': forms.Textarea(attrs={'rows': 4}),
        }
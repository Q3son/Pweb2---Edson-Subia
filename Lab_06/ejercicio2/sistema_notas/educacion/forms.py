from django import forms
from django.core.exceptions import ValidationError
from .models import Alumno, Curso, NotaAlumnoPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class NotaForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoPorCurso
        fields = ['alumno', 'curso', 'nota', 'fecha_evaluacion', 'observaciones']
        widgets = {
            'fecha_evaluacion': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        alumno = cleaned_data.get('alumno')
        curso = cleaned_data.get('curso')
        
        if alumno and curso:
            # Verificar si ya existe una nota para este alumno en este curso
            existe = NotaAlumnoPorCurso.objects.filter(
                alumno=alumno, 
                curso=curso
            ).exists()
            
            if existe and not self.instance.pk:
                raise ValidationError(
                    'Este alumno ya tiene una nota registrada para este curso'
                )
        
        return cleaned_data
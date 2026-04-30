"""
Formularios de la aplicación calificaciones_estudiantes.

Define CalificacionForm para crear y editar calificaciones,
y los formularios de autenticación de usuarios.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Calificacion


class CalificacionForm(forms.ModelForm):
    """
    Formulario basado en el modelo Calificacion.

    Excluye el campo 'promedio' ya que se calcula automáticamente.
    Incluye validaciones para que las notas estén entre 0.00 y 5.00.
    """

    class Meta:
        model = Calificacion
        exclude = ['promedio']
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del estudiante'
            }),
            'identificacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de identificación'
            }),
            'asignatura': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la asignatura'
            }),
            'nota1': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00 - 5.00',
                'step': '0.01',
                'min': '0',
                'max': '5'
            }),
            'nota2': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00 - 5.00',
                'step': '0.01',
                'min': '0',
                'max': '5'
            }),
            'nota3': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00 - 5.00',
                'step': '0.01',
                'min': '0',
                'max': '5'
            }),
        }

    def _validar_nota(self, campo):
        """Valida que una nota esté en el rango permitido (0.00 a 5.00)."""
        valor = self.cleaned_data.get(campo)
        if valor is not None:
            if valor < 0:
                raise forms.ValidationError('La nota no puede ser negativa.')
            if valor > 5:
                raise forms.ValidationError('La nota no puede ser mayor a 5.00.')
        return valor

    def clean_nota1(self):
        return self._validar_nota('nota1')

    def clean_nota2(self):
        return self._validar_nota('nota2')

    def clean_nota3(self):
        return self._validar_nota('nota3')


class RegistroUsuarioForm(UserCreationForm):
    """
    Formulario de registro de nuevos usuarios.

    Extiende UserCreationForm para incluir el campo email.
    """

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicar clase Bootstrap a los campos de contraseña
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

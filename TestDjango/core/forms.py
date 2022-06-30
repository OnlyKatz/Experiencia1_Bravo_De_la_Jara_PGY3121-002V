from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Vehiculo, Formulario


class ContactoForm(forms.ModelForm):

    class Meta:
        model= Formulario
        fields = ['nombre', 'apellido', 'correo', 'rut', 'telefono', 'comentario']
        labels ={
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'rut': 'Rut',
            'telefono': 'Telefono',
            'cuidad': 'Ciudad',
            'comentario': 'Comentario',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Nombre',
                    'id': 'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Apellido',
                    'id': 'apellido'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Correo',
                    'id': 'correo'
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Rut',
                    'id': 'rut'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Telefono',
                    'id': 'telefono'
                }
            ),
            'comentario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresar Comentario',
                    'id': 'comentario'
                }
            )
        }

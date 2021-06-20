from django import forms
from django.forms import ModelForm,widgets 
from .models import ComenUsuario

class ComentarioForm(ModelForm):

    class Meta: 
        model = ComenUsuario
        fields = ['idUser', 'nombreUser', 'titulo', 'texto','correo','deporte']
    
        labels={
            'idUser': 'ID_usuario:',
            'nombreUser': 'nombre:',
            'titulo': 'titulo:', 
            'texto': 'texto:',
            'correo': 'Correo:',
            'deporte': 'Deporte:',

        }
        widgets={
            'idUser': forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'id', 
                    'name': 'id',
                    'placeholder': 'id_usuario'
                }
            ),
            'nombreUser': forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'nombre', 
                    'placeholder': 'Nombre usuario'

                }
            ), 
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'titulo', 
                    'placeholder': 'titulo del tema'

                }
            ),
            'texto': forms.Textarea(
                attrs={
                    'class': 'form-titulo',
                    'id': 'cuadrotext'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'email'
                }
            ),
            'deporte': forms.Select(
                attrs={
                    'class': 'form-titulo',
                    'id': 'tipo'
                }
            ),
        }


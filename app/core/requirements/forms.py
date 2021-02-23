from core.user.models import User
from django.forms import ModelForm
from django.forms import *
from core.requirements.models import Requirements, Reasignado


class RequerimentsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = Requirements
        exclude = ['fechaAsignado', 'fechaAceptado', 'fechaTerminado', 'reasignar']
        widgets = {
            'tipe_req': TextInput(
                attrs={
                    'placeholder': 'Ingrese el tipo de requerimiento (*)',

                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Ingrese la descripción (*)',
                }
            ),
            'grupoUsuario': Select(
                attrs={
                    'placeholder': 'Seleccione un grupo (*)',
                    'class': 'grupos-class'
                }
            ),
            'estadoRequerimiento': Select(
                attrs={
                    'placeholder': 'Seleccione un estado (*)',
                    'class': 'estados-class'
                }
            ),
            'assign_to': Select(
                attrs={
                    'class': 'usuario-class'
                }
            ),
            'dueño': TextInput(
                attrs={
                    'class': 'dueño-req',
                    'readonly': 'readonly',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class UsuariosForm(ModelForm):
    class Meta:
        model = Reasignado
        exclude = ['fechaReasignado', ]
        widgets = {
            'usuarioReasignado': Select(
                attrs={
                    'placeholder': 'Seleccione un usuario',
                    'class': 'user-list form-control',
                    'id': 'user-list'

                }
            ),

        }

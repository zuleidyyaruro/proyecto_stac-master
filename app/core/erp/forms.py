from django.forms import *

from core.erp.models import Client, ClientEmp


class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'nombres': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombres (*)',
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'placeholder': 'Ingrese apellidos (*)',
                }
            ),
            'tipo_id': Select(
                attrs={
                'style': 'width: 100%',


            }),
            'identificacion': TextInput(
                attrs={
                    'placeholder': 'Ingrese Identificación (*)',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese dirección (*)',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese teléfono',
                }
            ),
            'celular': TextInput(
                attrs={
                    'placeholder': 'Ingrese celular (*)',
                }
            ),
            'whatsapp': TextInput(
                attrs={
                    'placeholder': 'Ingrese whatsapp',
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder': 'Ingrese correo electrónico (*)',
                    'type': 'email'
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

############################

class ClientEmpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = ClientEmp
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre de la empresa (*)',
                }
            ),
            'nit': TextInput(
                attrs={
                    'placeholder': 'Ingrese NIT de la empresa (*)',
                }
            ),
            'pais': TextInput(
                attrs={
                    'placeholder': 'Ingrese el pais (*)',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese dirección',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese numero telefonico',
                }
            ),
            'whatsapp': TextInput(
                attrs={
                    'placeholder': 'Ingrese whatsapp',
                }
            ),
            'correo': TextInput(
                attrs={
                    'placeholder': 'Ingrese correo electronico (*)',
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


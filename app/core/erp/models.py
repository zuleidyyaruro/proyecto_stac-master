from django.db import models
from django.forms import model_to_dict

from config.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import identificacion_choices

class Client(models.Model):

    nombres=models.CharField(max_length=150, verbose_name="Nombres")
    apellidos=models.CharField(max_length=150, verbose_name="Apellidos")
    tipo_id=models.CharField(max_length=25, choices=identificacion_choices, default='Cedula', verbose_name="Tipo Id")
    identificacion=models.CharField(max_length=30, verbose_name="Identificación", unique=True)
    direccion=models.CharField(max_length=150, verbose_name="Direccion")
    telefono=models.CharField(max_length=15, verbose_name="Teléfono", blank=True, null=True, default="---")
    celular=models.CharField(max_length=15, verbose_name="Celular")
    whatsapp=models.CharField(max_length=15, verbose_name="WSP", blank=True, null=True, default="---")
    correo=models.CharField(max_length=150, unique=True, verbose_name="Correo")

    def __str__(self):
        return self.nombres

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural="Clientes"
        ordering = ['id']


class ClientEmp(models.Model):

    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    nit = models.CharField(max_length=150, unique=True, verbose_name='NIT')
    pais = models.CharField(max_length=150, verbose_name='Pais')
    direccion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    telefono = models.CharField(max_length=150, null=True, blank=True, verbose_name='Telefono')
    whatsapp=models.CharField(max_length=15, verbose_name="WSP", blank=True, null=True)
    correo = models.CharField(max_length=150, unique=True,  verbose_name='Correo')
    image = models.ImageField(upload_to='clientEmp/%Y/%m/%d', null=True, blank=True, verbose_name='Logo')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'ClienteEmp'
        verbose_name_plural = 'ClientesEmp'
        ordering = ['id']
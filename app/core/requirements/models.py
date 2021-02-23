from django.db import models
from django.contrib.auth.models import Group
from core.user.models import User

from django.conf import settings
from datetime import datetime

class Estados (models.Model):
    
    estados=models.CharField(max_length=150, verbose_name="Estados")

    def __str__(self):
        return self.estados

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = "Estados"
        ordering = ['id']

class Requirements (models.Model):
    dueño = models.CharField(max_length=150, verbose_name="Dueño", null=True, blank=True)
    tipe_req=models.CharField(max_length=150, verbose_name="Requerimiento")
    description=models.CharField(max_length=1000, verbose_name="Descripción")
    grupoUsuario = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Grupos', null=True, blank=True)
    assign_to=models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,  on_delete=models.CASCADE, verbose_name="Asignar")
    estadoRequerimiento = models.ForeignKey(Estados, on_delete=models.CASCADE, verbose_name='Estado', null=True, blank=True)
    file=models.FileField(upload_to='files/%Y/%m/%d', null=True, blank=True)
    fechaAsignado = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Asignación')
    fechaAceptado = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Aceptación')
    fechaTerminado = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Terminado')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Requerimiento'
        verbose_name_plural = "Requerimientos"
        ordering = ['id']


class Reasignado(models.Model):
    requerimiento = models.ForeignKey(Requirements, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Requerimiento')
    usuarioReasignado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario Reasignado")
    fechaReasignado = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Asignación')

    def __str__(self):
        return str(self.usuarioReasignado)
       


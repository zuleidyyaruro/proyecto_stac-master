from django.contrib import admin
from core.requirements.models import Requirements, Estados, Reasignado


#PErsonalizar el modelo de requerimientos
class CustomRequirements(admin.ModelAdmin):
    list_display = ['dueño','tipe_req', 'description', 'grupoUsuario', 'assign_to', 'estadoRequerimiento', 'file', 'fechaAsignado', 'fechaAceptado', 'fechaTerminado']
    search_fields = ['tipe_req']
    list_filter = ['grupoUsuario', 'dueño']
    list_per_page = 10

#PErsonalizar el modelo de requerimientos Reasignados
class CustomRequirementsReasignados(admin.ModelAdmin):
    list_display = ['requerimiento','usuarioReasignado', 'fechaReasignado']
    search_fields = ['usuarioReasignado', 'requerimiento']
    list_filter = ['usuarioReasignado']
    list_per_page = 10


admin.site.register(Requirements,CustomRequirements)
admin.site.register(Estados)
admin.site.register(Reasignado, CustomRequirementsReasignados)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView

import json
from datetime import datetime

from core.erp.mixins import ValidatePermissionRequiredMixin
from core.requirements.forms import RequerimentsForm, UsuariosForm
from core.requirements.models import Estados, Requirements, Reasignado
from core.user.models import User
from django.contrib.auth.models import Group


class RequirementsCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Requirements
    form_class = RequerimentsForm
    template_name = 'create.html'
    success_url = reverse_lazy('requirements.requirements_create')
    permission_required = 'requirements.add_requirements'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()

            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de un Requerimiento'
        context['entity'] = 'Requerimientos'
        # context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


@login_required
def ObtenerUsuarios(request, id):
    try:
        grupo = Group.objects.get(id=id)
        usuarios = grupo.user_set.all()
        listaUsuarios = []
        for i in usuarios:
            listaUsuarios.append({'id': str(i.id), 'text': i.username})
        return HttpResponse(json.dumps(listaUsuarios))
    except Exception as e:
        print(e)
        return HttpResponseBadRequest(json.dumps({'Error': 'Ha ocurrido un error interno.'}))


@login_required
def listarRequerimientosAdmin(request):
    queryset = Requirements.objects.all()
    data = {
        'requerimientos': queryset
    }
    return render(request, 'lista_requerimientos_admin.html', data)


@login_required
def listarRequerimientosUser(request):
    queryset = Requirements.objects.filter(assign_to=request.user).exclude(estadoRequerimiento=4)

    data = {
        'requerimientos': queryset, 'form': UsuariosForm()
    }
    return render(request, 'lista_requerimientos_user.html', data)


@login_required
@csrf_exempt
def ActualizarEstado(request, id, estado):
    if request.is_ajax():
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                idReasignado = data['reasignadoId']
            except Exception as e:
                print(e)

            try:
                fechaActual = datetime.now()

                if estado == '2':
                    estadoN = Estados.objects.get(id=int(estado))
                    requerimiento = Requirements.objects.get(id=int(id))
                    requerimiento.estadoRequerimiento = estadoN
                    requerimiento.fechaAceptado = fechaActual
                    requerimiento.save()

                if estado == '3':
                    estadoN = Estados.objects.get(id=int(estado))
                    requerimiento = Requirements.objects.get(id=int(id))
                    requerimiento.estadoRequerimiento = estadoN
                    requerimiento.fechaTerminado = fechaActual
                    requerimiento.save()

                if estado == '4':
                    estadoN = Estados.objects.get(id=int(estado))
                    requerimiento = Requirements.objects.get(id=int(id))
                    requerimiento.estadoRequerimiento = estadoN
                    requerimiento.save()
                    reasigna = Reasignado()
                    reasigna.usuarioReasignado_id = int(idReasignado)
                    reasigna.requerimiento_id = int(id)
                    reasigna.save()

                return HttpResponse(json.dumps({'message': 'hola '}))

            except Exception as e:
                print(e)
                return HttpResponseBadRequest(json.dumps({'Error': 'Ha ocurrido un error interno.'}))

@login_required
def timeline(request, id):
    queryset = Requirements.objects.get(id=int(id))
    reasignacion = Reasignado.objects.filter(requerimiento=queryset)
    fechaReasignado = ''
    usuarioReasignado = ''
    for i in reasignacion:
        fechaReasignado = i.fechaReasignado.strftime('%x %H:%M:%S')
        usuarioReasignado = i.usuarioReasignado

    fechaAsignado = queryset.fechaAsignado.strftime('%x %H:%M:%S')
    fechaAceptado = queryset.fechaAceptado.strftime('%x %H:%M:%S')
    fechaTerminado = queryset.fechaTerminado.strftime('%x %H:%M:%S')

    data = {
        'requerimiento': queryset,
        'fechaAsignado': fechaAsignado,
        'fechaAceptado': fechaAceptado,
        'fechaTerminado': fechaTerminado,
        'fechaReasignado': fechaReasignado,
        'usuarioReasignado': usuarioReasignado
    }
    return render(request, 'timeline.html', data)


@login_required
def listarRequerimientosAsignadosUser(request):
    queryset = Reasignado.objects.filter(usuarioReasignado=request.user)

    data = {
        'reasignados': queryset
    }

    return render(request, 'reasignados.html', data)

class IndexView(TemplateView):
    template_name = "requirements/indexr.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

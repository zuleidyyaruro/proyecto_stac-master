from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ClientEmpForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import ClientEmp

class ClientEmpListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = ClientEmp
    template_name = 'client2/list.html'
    permission_required = 'erp.view_clientemp'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in ClientEmp.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes-Empresa'
        context['create_url'] = reverse_lazy('erp:clientemp_create')
        context['list_url'] = reverse_lazy('erp:clientemp_list')
        context['entity'] = 'ClientesEmp'
        return context


class ClientEmpCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = ClientEmp
    form_class = ClientEmpForm
    template_name = 'client2/create.html'
    success_url = reverse_lazy('erp:clientemp_list')
    permission_required = 'erp.add_clientemp'
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
        context['title'] = 'Registro de un Cliente-Empresa'
        context['entity'] = 'ClientesEmp'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ClientEmpUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = ClientEmp
    form_class = ClientEmpForm
    template_name = 'client2/create.html'
    success_url = reverse_lazy('erp:clientemp_list')
    permission_required = 'erp.change_clientemp'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición un Cliente'
        context['entity'] = 'ClientesEmp'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ClientEmpDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = ClientEmp
    template_name = 'client2/delete.html'
    success_url = reverse_lazy('erp:clientemp_list')
    permission_required = 'erp.delete_clientemp'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Cliente'
        context['entity'] = 'ClientesEmp'
        context['list_url'] = self.success_url
        return context

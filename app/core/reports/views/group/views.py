from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.reports.forms import ReportForm
from core.requirements.models import Requirements


class ReportGroupsViews(TemplateView):
    template_name ="groups/report.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Requirements.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fechaAsignado__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.tipe_req,
                        s.grupoUsuario.name,
                        s.fechaAsignado.strftime('%Y-%m-%d'),
                    ])

                totalGestor=search.filter(grupoUsuario__name__exact="Gestor").count()
                totalComercial= search.filter(grupoUsuario__name__exact="Comercial").count()

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                ])

                data.append([
                    '---',
                    '---',
                    'Total Requerimientos Gestor: ',
                    totalGestor,
                ])

                data.append([
                    '---',
                    '---',
                    'Total Requerimientos Comercial: ',
                    totalComercial,
                ])

                mayor=""
                if(totalGestor>totalComercial):
                    mayor="Gestor"
                elif(totalGestor<totalComercial):
                    mayor= "Comercial"
                else:
                    mayor = ""

                data.append([
                    '---',
                    '---',
                    'Grupo con mas requerimientos: ',
                    mayor,
                ])


            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de requeremientos por Grupos'
        context["form"] = ReportForm()
        return context


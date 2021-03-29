from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.reports.forms import ReportForm
from core.requirements.models import Requirements


class ReportRequirementViews(TemplateView):
    template_name ="requirements/report.html"

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
                        s.dueño,
                        s.tipe_req,
                        s.grupoUsuario.name,
                        s.assign_to.username,
                        s.estadoRequerimiento.estados,
                        s.fechaAsignado.strftime('%Y-%m-%d'),
                    ])

                total = search.count()

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    '---',
                    '---',
                    '---',

                ])

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    '---',
                    'Total Requerimientos": ',
                    total,
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


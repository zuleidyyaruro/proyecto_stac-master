from django.urls import path

from core.reports.views import ReportRequirementsView, IndexViewReport

app_name = 'reports'

urlpatterns = [

    path('', IndexViewReport.as_view(), name='index-report'),
    path("requirement", ReportRequirementsView.as_view(), name="requirement_report")

]

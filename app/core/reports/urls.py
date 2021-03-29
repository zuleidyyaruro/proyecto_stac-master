from django.urls import path

from core.reports.views.group.views import ReportGroupsViews
from core.reports.views.index.views import IndexViewReport
from core.reports.views.requirement.views import ReportRequirementViews

from core.reports.views.states.views import ReportStatesViews

app_name = 'reports'

urlpatterns = [

    path('', IndexViewReport.as_view(), name='index-report'),
    path('requirement', ReportRequirementViews.as_view(), name='requirements-report'),
    #path("requirement", ReportRequirementViews.as_view(), name="requirement_report"),
    path("group", ReportGroupsViews.as_view(), name="group_report"),
    path("states", ReportStatesViews.as_view(), name="state_report")

]

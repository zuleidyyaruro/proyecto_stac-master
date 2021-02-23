from django.urls import path

from core.erp.views.client.views import *
from core.erp.views.client2.views import *

app_name = 'erp'

urlpatterns = [

    path('', IndexView.as_view(), name='indexc'),
    # Cliente Persona
    path('client/list/', ClientListView.as_view(), name="client_list"),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    ######Cliente EMPRESA##############
    path('clientemp/list/', ClientEmpListView.as_view(), name='clientemp_list'),
    path('clientemp/add/', ClientEmpCreateView.as_view(), name='clientemp_create'),
    path('clientemp/update/<int:pk>/', ClientEmpUpdateView.as_view(), name='clientemp_update'),
    path('clientemp/delete/<int:pk>/', ClientEmpDeleteView.as_view(), name='clientemp_delete'),
]

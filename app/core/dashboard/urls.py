from django.urls import path, include

from core.dashboard import views
from core.dashboard.views import *


urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', include('core.login.urls')),
    path('ver-usuario', views.usuario, name='usuario'),

]
from django.urls import path

from core.requirements.views import RequirementsCreateView, ObtenerUsuarios, listarRequerimientosAdmin, \
    listarRequerimientosUser, ActualizarEstado, timeline, listarRequerimientosAsignadosUser, IndexView

app_name="requirements"

urlpatterns=[
    path('requirement/add/', RequirementsCreateView.as_view(), name="requirements_create"),
    path('obtener-usuarios/<id>/',ObtenerUsuarios , name="obtener_usuarios"),
    path('requirement/list-admin/',listarRequerimientosAdmin , name="lista_requirement_admin"),
    #
    path('requirement/list-user/',listarRequerimientosUser , name="lista_requirement_user"),
    #
    path('requirement/list-reasignados/',listarRequerimientosAsignadosUser , name="lista_requirement_reasignados"),
    path('requirement/update-estado/<id>/<estado>/',ActualizarEstado , name="update_estado"),
    path('requirement/timeline/<id>/',timeline , name="timeline"),
    path('', IndexView.as_view(), name="indexr")
   

]
from django.urls import path, include
from api.views.usuarios_views import *

#en estas urls son los enlaces hacia los metodos del api
urlpatterns = [

    path("usuarios/", usuario_api_view, name='usuarios_api'),
    path("usuarios/<int:pk>/", usuario_detalle_api_view, name='usuario_detalle_api_view'),
    path("estudiantes/", estudiantes_api_view, name='estudiantes_api'),
    path("estudiantes/<int:pk>/", estudiante_detalle_api_view, name='estudiante_detalle_api_view'),
    path("administradores/", administradores_api_view, name='administradores_api'),
    path("administradores/<int:pk>/", administrador_detalle_api_view, name='administrador_detalle_api_view'),
]
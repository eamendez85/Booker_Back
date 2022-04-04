from django.urls import path, include
from api.views import *

#en estas urls son los enlaces hacia los metodos del api
urlpatterns = [

    path("usuarios/", usuario_api_view, name='usuarios_api'),
    path("usuarios/<int:pk>/", usuario_detalle_api_view, name='usuario_detalle_api_view')
]
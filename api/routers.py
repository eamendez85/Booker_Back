from email.mime import base
from django import urls
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from api.views.general_views import AutoresViewset, CategoriasViewSet, EditorialesViewSet, GradoViewSet, GruposViewSet

router = DefaultRouter()

router.register(r'grados', GradoViewSet, basename= 'grados')
router.register(r'grupos', GruposViewSet, basename= 'grupos')
router.register(r'categorias', CategoriasViewSet, basename= 'categorias')
router.register(r'autores', AutoresViewset, basename= 'autores')
router.register(r'editoriales', EditorialesViewSet, basename= 'editoriales')

urlpatterns = router.urls
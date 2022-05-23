from email.mime import base
from django import urls
from django.urls import URLPattern
from rest_framework.routers import DefaultRouter
from api.views.general_views import *
from api.views.usuarios_views import UsuariosViewSet, EstudiantesViewSet
from api.views.libros_views import LibrosViewSet

router = DefaultRouter()

router.register(r'grados', GradoViewSet, basename= 'grados')
router.register(r'grupos', GruposViewSet, basename= 'grupos')
router.register(r'categorias', CategoriasViewSet, basename= 'categorias')
router.register(r'autores', AutoresViewset, basename= 'autores')
router.register(r'editoriales', EditorialesViewSet, basename= 'editoriales')
router.register(r'idiomas', IdiomasViewSet, basename= 'idiomas')
router.register(r'favoritos', FavoritosViewSet, basename= 'favoritos')
router.register(r'ejemplares', EjemplaresViewSet, basename= 'ejemplares')
router.register(r'tipoInfraccion', TipoInfraccionViewSet, basename= 'tipoInfraccion')
router.register(r'infracciones', InfraccionesViewSet, basename= 'infracciones')
router.register(r'prestamos', DetallePrestamoViewSet, basename= 'prestamos')
router.register(r'libros', LibrosViewSet, basename= 'libros')
router.register(r'reservas', ReservasViewSet, basename= 'reservas')
router.register(r'usuarios', UsuariosViewSet, basename= 'usuarios')
router.register(r'estudiantes', EstudiantesViewSet, basename= 'estudiantes')


urlpatterns = router.urls
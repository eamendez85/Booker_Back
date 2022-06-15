from django.contrib import admin
from django.urls import path, include
from api.views.importar_csv_estudiantes import importar_csv_estudiantes
from api.views.login_logout_views import Login, Logout, UserToken
from django.conf.urls.static import static
from api.views.csv_views import CsvCreateApiView
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('modulos/', include('api.routers')),
    path('importar-estudiantes/', CsvCreateApiView.as_view(), name="importar estudiantes"),
    path('', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    
    #Enviar parametro {'doc':'sdsd'}
    path('refresh-token/', UserToken.as_view(), name='refresh_token'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

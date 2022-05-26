from django.contrib import admin
from django.urls import path, include
from api.views.login_logout_views import Login, Logout, UserToken
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('modulos/', include('api.routers')),
    path('', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    
    #Enviar parametro {'doc':'sdsd'}
    path('refresh-token/', UserToken.as_view(), name='refresh_token'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from api.views.login_views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('modulos/', include('api.routers')),
    path('', Login.as_view(), name='Login'),
]

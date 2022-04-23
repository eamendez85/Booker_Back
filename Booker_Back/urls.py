from django.contrib import admin
from django.urls import path, include
from api.views.login_logout_views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('modulos/', include('api.routers')),
    path('', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
]

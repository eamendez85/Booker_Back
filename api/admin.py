from django.contrib import admin

from api.models import Usuario

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display=('doc', 'name')

admin.site.register(Usuario, UsuariosAdmin)
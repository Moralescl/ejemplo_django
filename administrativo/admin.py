from django.contrib import admin

# Register your models here.

from administrativo.models import Estudiante, NumeroTelefonico

#admin.site.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','cedula')
    search_fields = ('nombre','cedula')

admin.site.register(Estudiante,EstudianteAdmin)

#admin.site.register(NumeroTelefonico)

class NumeroTelefonoAdmin(admin.ModelAdmin):
    list_display = ('telefono','tipo','get_estudiante')
    raw_id_fields = ('estudiante',)
    def get_estudiante(self, obj):
        """ """
        return obj.estudiante.apellido
    
admin.site.register(NumeroTelefonico,NumeroTelefonoAdmin)
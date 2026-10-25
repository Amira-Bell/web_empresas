from django.contrib import admin
from .models import Persona


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'titulo_academico', 'correo_electronico', 'telefono')

    def has_add_permission(self, request):
        # Solo se permite un único registro de Persona
        return not Persona.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Evita borrar el único registro por accidente
        return False


admin.site.register(Persona, PersonaAdmin)

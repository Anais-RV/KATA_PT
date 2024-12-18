from django.contrib import admin
from zombies.models import Superviviente, Equipo

@admin.register(Superviviente)
class SupervivienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass

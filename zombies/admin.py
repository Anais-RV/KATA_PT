from django.contrib import admin
from zombies.models import Superviviente, Equipo, Partida

@admin.register(Superviviente)
class SupervivienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['jugador', 'supervivientes_count']
    
    def supervivientes_count(self, obj):
        return obj.supervivientes.count()
    supervivientes_count.short_description = 'Supervivientes'
    pass

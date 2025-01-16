from django.urls import path
from zombies.views.supervivientes import SupervivientesView  
from zombies.views.equipo import EquipoView 
from zombies.views.partida import PartidasView

urlpatterns = [
    path('supervivientes/', SupervivientesView.as_view(), name='supervivientes'),
    path('equipo/', EquipoView.as_view(), name='equipo'),
    path('partidas/', PartidasView.as_view(), name='partidas'),
]

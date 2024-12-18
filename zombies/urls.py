from django.urls import path
from zombies.views.supervivientes import SupervivientesView  
from zombies.views.equipo import EquipoView 

urlpatterns = [
    path('supervivientes/', SupervivientesView.as_view(), name='supervivientes'),
    path('equipo/', EquipoView.as_view(), name='equipo'),
]

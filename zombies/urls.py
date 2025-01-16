# from django.urls import path, include  
# from rest_framework.routers import DefaultRouter
# from zombies.views.supervivientes import SupervivientesView  
# from zombies.views.equipo import EquipoView 
# from zombies.views.partida import PartidasView

# router = DefaultRouter()

# urlpatterns = [
#     path('api/', include(router.urls)),  # Rutas generadas automáticamente para PartidasView
#     path('api/supervivientes/', SupervivientesView.as_view(), name='supervivientes'),
#     path('api/equipo/', EquipoView.as_view(), name='equipo'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from zombies.views.partida import PartidasView
from zombies.views.supervivientes import SupervivientesView
from zombies.views.equipo import EquipoView

router = DefaultRouter()
router.register(r'partidas', PartidasView, basename='partidas')
router.register(r'supervivientes', SupervivientesView, basename='supervivientes')
router.register(r'equipo', EquipoView, basename='equipo')

urlpatterns = [
    path('', include(router.urls)),
]



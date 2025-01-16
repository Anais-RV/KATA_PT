from rest_framework.viewsets import ModelViewSet
from zombies.models import Partida
from zombies.serializers import PartidaSerializer

class PartidasView(ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

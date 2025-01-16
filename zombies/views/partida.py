from rest_framework.views import APIView
from rest_framework.response import Response
from zombies.models import Partida
from zombies.serializers import PartidaSerializer

class PartidasView (APIView):
    def get(self, request):
        partidas = Partida.objects.all()
        serializer = PartidaSerializer(partidas, many=True)
        return Response(serializer.data)
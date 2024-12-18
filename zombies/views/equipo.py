from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from zombies.models import Equipo
from zombies.serializers import EquipoSerializer

class EquipoView(APIView):
    def get(self, request):
        equipo = Equipo.objects.all()
        serializer = EquipoSerializer(equipo, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

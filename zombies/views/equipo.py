from django.core.exceptions import ValidationError
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
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                # Capturamos ValidationError y devolvemos un código 400 con el mensaje de error
                return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)
        # Si el serializer no es válido
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

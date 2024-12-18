from rest_framework.views import APIView
from rest_framework.response import Response
from zombies.models import Superviviente
from zombies.serializers import SupervivienteSerializer
from rest_framework import status

class SupervivientesView(APIView):
    def get(self, request):
        # Obtenemos todos los supervivientes
        supervivientes = Superviviente.objects.all()
        serializer = SupervivienteSerializer(supervivientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Creamos un nuevo superviviente
        serializer = SupervivienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

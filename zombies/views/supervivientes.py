from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from zombies.models import Superviviente
from zombies.serializers import SupervivienteSerializer
from rest_framework import status

class SupervivientesView(ModelViewSet):
    queryset = Superviviente.objects.all()
    serializer_class = SupervivienteSerializer

    def post(self, request):
        # Creamos un nuevo superviviente
        serializer = SupervivienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

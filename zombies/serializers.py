from rest_framework import serializers
from zombies.models import Superviviente, Equipo

class SupervivienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superviviente
        fields = ['id', 'nombre', 'heridas', 'acciones', 'experiencia', 'nivel']

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'tipo', 'superviviente']

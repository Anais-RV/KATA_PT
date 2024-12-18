from django.db import models
from .superviviente import Superviviente

class Equipo(models.Model):
    TIPO_EQUIPO = [
        ("Mano", "En Mano"),
        ("Reserva", "En Reserva"),
    ]

    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10, choices=TIPO_EQUIPO, default="Mano")
    superviviente = models.ForeignKey(Superviviente, on_delete=models.CASCADE, related_name="equipo")

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

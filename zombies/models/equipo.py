from django.core.exceptions import ValidationError
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

    def validar_tipo(self):
        """Validamos el tipo de equipo."""
        tipos_validos = [tipo for tipo, _ in self.TIPO_EQUIPO]
        if self.tipo not in tipos_validos:
            raise ValidationError(f"El tipo de equipo '{self.tipo}' no es válido. Opciones: {tipos_validos}")

    def save(self, *args, **kwargs):

        # Validar el tipo de equipo
        self.validar_tipo()

        # Validar que no haya más de 2 piezas "En Mano"
        if self.tipo == "Mano" and self.superviviente.equipo.filter(tipo="Mano").count() >= 2:
            raise ValidationError("Un superviviente no puede llevar más de 2 piezas en Mano.")
        
        # Validar que no haya más de 5 piezas totales
        if self.superviviente.equipo.count() >= 5:
            raise ValidationError("Un superviviente no puede llevar más de 5 piezas de equipo.")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

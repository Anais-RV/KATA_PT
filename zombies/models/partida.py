from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from .superviviente import Superviviente


class Partida(models.Model):
    jugador = models.CharField(max_length=100, unique=True)
    supervivientes = models.ManyToManyField('Superviviente', related_name='partidas', blank=True)
    finalizada = models.BooleanField(default=False)
    nivel = models.CharField(max_length=50, default='Azul', choices=Superviviente.NIVELES)

    def actualizar_estado(self):
        """
        Actualiza el estado de la partida. Si todos los supervivientes están muertos,
        la partida se marca como finalizada.
        """
        if self.supervivientes.exists():  # Asegúrate de que hay supervivientes
            self.finalizada = all(s.esta_muerto() for s in self.supervivientes.all())
        else:
            self.finalizada = False  # Si no hay supervivientes, no se finaliza
        self.save()
    
    def actualizar_nivel(self):
        """El nivel de la partida es igual al nivel más alto entre los supervivientes vivos."""
        supervivientes_vivos = self.supervivientes.filter(vivo=True)  # Filtrar solo vivos
        print(f"Supervivientes vivos: {[s.nombre for s in supervivientes_vivos]}")

        niveles = [s.nivel for s in supervivientes_vivos]
        print(f"Niveles de supervivientes vivos: {niveles}")

        if niveles:
            niveles_ordenados = ['Azul', 'Amarillo', 'Naranja', 'Rojo']
            self.nivel = max(niveles, key=lambda nivel: niveles_ordenados.index(nivel))
        else:
            self.nivel = 'Azul'  # Si no hay supervivientes vivos, nivel es Azul

        print(f"Nivel calculado para la partida: {self.nivel}")
        self.save()

    def __str__(self):
        return self.jugador


@receiver(m2m_changed, sender=Partida.supervivientes.through)
def validar_supervivientes_unicos(sender, instance, action, pk_set, **kwargs):
    """
    Valida que los nombres de los supervivientes en la partida sean únicos.
    """
    if action == "post_add":
        supervivientes_actuales = instance.supervivientes.exclude(pk__in=pk_set)
        supervivientes_nuevos = Superviviente.objects.filter(pk__in=pk_set)
        nombres = [s.nombre for s in supervivientes_actuales] + [s.nombre for s in supervivientes_nuevos]
        if len(nombres) != len(set(nombres)):
            raise ValidationError("Los nombres de los supervivientes deben ser únicos dentro de la partida.")


@receiver(post_save, sender=Superviviente)
def actualizar_estado_partidas(sender, instance, **kwargs):
    """
    Cada vez que se guarda un superviviente, actualiza las partidas relacionadas.
    """
    for partida in instance.partidas.all():
        partida.actualizar_estado()
        partida.actualizar_nivel()

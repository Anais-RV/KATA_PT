from django.db import models
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.dispatch import receiver

class Partida(models.Model):
    jugador = models.CharField(max_length=100, unique=True)
    supervivientes = models.ManyToManyField('Superviviente', related_name='partidas', blank=True)

    def __str__(self):
        return self.jugador


@receiver(m2m_changed, sender=Partida.supervivientes.through) # disparar la señal m2m_changed cada vez que se modifique la relación de muchos a muchos entre Partida y Superviviente
def validar_supervivientes_unicos(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        nombres = [superviviente.nombre for superviviente in instance.supervivientes.all()]
        if len(nombres) != len(set(nombres)):
            raise ValidationError("Los nombres de los supervivientes deben ser únicos dentro de la partida.")

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Superviviente(models.Model):
    NIVELES = [
        ('Azul', 'Azul'),
        ('Amarillo', 'Amarillo'),
        ('Naranja', 'Naranja'),
        ('Rojo', 'Rojo'),
    ]

    nombre = models.CharField(max_length=50, unique=True)
    heridas = models.IntegerField(default=0)
    acciones = models.IntegerField(default=3)
    experiencia = models.IntegerField(default=0)
    nivel = models.CharField(max_length=50, choices=NIVELES, default='Azul')
    vivo = models.BooleanField(default=True)

    def esta_muerto(self):
        """Devuelve True si el superviviente ha muerto"""
        return self.heridas >= 2

    def capacidad_equipo(self):
        """Calcula la capacidad máxima de equipo según las heridas"""
        return max(5 - self.heridas, 0)

    def verificar_equipo(self):
        """Elimina piezas de equipo si exceden la capacidad máxima"""
        capacidad = self.capacidad_equipo()
        while self.equipo.count() > capacidad:
            pieza_a_descartar = self.equipo.filter(tipo="Reserva").first()
            if not pieza_a_descartar:
                pieza_a_descartar = self.equipo.first()
            pieza_a_descartar.delete()

    def save(self, *args, **kwargs):
        """Asegura que el atributo 'vivo' refleja el estado actual del superviviente"""
        self.vivo = not self.esta_muerto()
        super().save(*args, **kwargs)
        self.verificar_equipo()

    def __str__(self):
        return f"{self.nombre} ({'Muerto' if self.esta_muerto() else 'Vivo'})"

# Señal para actualizar las partidas relacionadas cuando se guarda un Superviviente
@receiver(post_save, sender=Superviviente)
def actualizar_estado_partida(sender, instance, **kwargs):
    """Actualiza el estado de las partidas relacionadas con el superviviente"""
    for partida in instance.partidas.all():
        partida.actualizar_estado()

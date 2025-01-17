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
    
    def esta_vivo(self):
        """Devuelve True si el superviviente está vivo."""
        print(f"Comprobando si {self.nombre} está vivo: {self.vivo}")
        return self.vivo

    def capacidad_equipo(self):
        """Calcula la capacidad máxima de equipo según las heridas"""
        return max(5 - self.heridas, 0)

    def verificar_equipo(self):
        """Elimina piezas de equipo si exceden la capacidad máxima."""
        capacidad = self.capacidad_equipo()
        equipo_actual = self.equipo.all()
        exceso = equipo_actual.count() - capacidad  # Número de piezas a eliminar

        print(f"Capacidad actual: {capacidad}, Piezas actuales: {equipo_actual.count()}, Exceso: {exceso}")

        if exceso > 0:
            piezas_a_eliminar = self.equipo.filter(tipo="Reserva")[:exceso]  # Prioriza tipo "Reserva"
            for pieza in piezas_a_eliminar:
                pieza.delete()
            
            # Si aún hay exceso, elimina otras piezas
            exceso_restante = self.equipo.all().count() - capacidad
            if exceso_restante > 0:
                piezas_adicionales = self.equipo.all()[:exceso_restante]
                for pieza in piezas_adicionales:
                    pieza.delete()
    
    def actualizar_nivel(self):
        """Actualiza el nivel del superviviente según la experiencia"""
        if self.experiencia >= 43:
            self.nivel = 'Rojo'
        elif self.experiencia >= 19:
            self.nivel = 'Naranja'
        elif self.experiencia >= 7:
            self.nivel = 'Amarillo'
        else:
            self.nivel = 'Azul'

    def save(self, *args, **kwargs):
        """Actualiza el estado antes de guardar."""
        self.vivo = not self.esta_muerto()
        print(f"Guardando {self.nombre}: vivo={self.vivo}, heridas={self.heridas}")
        self.actualizar_nivel()
        super().save(*args, **kwargs)
        self.verificar_equipo()  # Llama a verificar_equipo después de guardar



    def __str__(self):
        return f"{self.nombre} ({'Muerto' if self.esta_muerto() else 'Vivo'})"

# Señal para actualizar las partidas relacionadas cuando se guarda un Superviviente
@receiver(post_save, sender=Superviviente)
def actualizar_estado_partida(sender, instance, **kwargs):
    """Actualiza el estado de las partidas relacionadas con el superviviente"""
    for partida in instance.partidas.all():
        partida.actualizar_estado()

from django.db import models

class Superviviente(models.Model):
    NIVELES = [
        ('Azul', 'Azul'),
        ('Amarillo', 'Amarillo'),
        ('Naranja', 'Naranja'),
        ('Rojo', 'Rojo'),
    ]

    nombre = models.CharField(max_length=50)
    heridas = models.IntegerField(default=0)
    acciones = models.IntegerField(default=3)
    experiencia = models.IntegerField(default=0)
    nivel = models.CharField(max_length=50, choices=NIVELES, default='Azul')

    def esta_muerto(self):
        """ Devuelve True si el superviviente ha muerto """
        return self.heridas >= 2

    def capacidad_equipo(self):
        """ Calcula la capacidad máxima de equipo según las heridas """
        return max(5 - self.heridas, 0)

    def verificar_equipo(self):
        """ Elimina piezas de equipo si exceden la capacidad máxima """
        capacidad = self.capacidad_equipo()
        while self.equipo.count() > capacidad:
            # Elimina primero las piezas "En Reserva"
            pieza_a_descartar = self.equipo.filter(tipo="Reserva").first()
            if not pieza_a_descartar:
                # Si no hay más piezas "En Reserva", elimina "En Mano"
                pieza_a_descartar = self.equipo.first()
            pieza_a_descartar.delete()

    def save(self, *args, **kwargs):
        """ Guarda el objeto y ajusta el equipo si es necesario """
        super().save(*args, **kwargs)
        self.verificar_equipo()

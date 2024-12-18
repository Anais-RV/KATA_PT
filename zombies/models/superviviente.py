from django.db import models

class Superviviente(models.Model):
    NIVELES = [
        ('Azul', 'Azul'),
        ('Amarillo', 'Amarillo'),
        ('Naranja', 'Naranja'),
        ('Rojo', 'Rojo')
    ]

    nombre = models.CharField(max_length=50)
    heridas = models.IntegerField(default=0)
    acciones = models.IntegerField(default=3)
    experiencia = models.IntegerField(default=0)
    nivel = models.CharField(max_length=50, choices=NIVELES, default='Azul')

    def esta_muerto(self):

        """ Devuelve True si el superviviente ha muerto """
        return self.heridas >= 2
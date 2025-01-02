# from django.db import models

# class Partida(models.Model):
#     nombre = models.CharField(max_length=100, unique=True)
#     supervivientes = models.ManyToManyField('Superviviente', related_name='partidas', blank=True)
#     def __str__(self):
#         return self.nombre
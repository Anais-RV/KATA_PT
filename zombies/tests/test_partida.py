from django.test import TestCase
from zombies.models import Partida, Jugador, Zombi, JugadorPartidaº

class PartidaTestCase(TestCase):
    def test_partida_comienza_sin_supervivientes(self):
        partida = Partida()
        self.assertEqual(partida.supervivientes.count(), 0)
        return super().partida_comienza_sin_supervivientes()
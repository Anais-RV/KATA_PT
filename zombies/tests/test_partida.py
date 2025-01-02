from django.test import TestCase
from zombies.models import Partida

class PartidaTestCase(TestCase):
    def test_partida_comienza_sin_supervivientes(self):
        """Test para verificar que una partida comienza con 0 supervivientes."""
        partida = Partida.objects.create(jugador="Jugador 1")  
        self.assertEqual(partida.supervivientes.count(), 0)

from django.test import TestCase
from zombies.models import Partida

class PartidaTestCase(TestCase):
    def test_partida_comienza_sin_supervivientes(self):
        """Test para verificar que una partida comienza con 0 supervivientes."""
        partida = Partida.objects.create(jugador="Jugador 1")  
        self.assertEqual(partida.supervivientes.count(), 0)

    def test_añadir_supervivientes_a_partida(self):
        """Test para verificar que una partida puede tener supervivientes."""
        partida = Partida.objects.create(jugador="Jugador 1")
        
        # Crear supervivientes
        superviviente1 = partida.supervivientes.create(nombre="Superviviente 1")
        superviviente2 = partida.supervivientes.create(nombre="Superviviente 2")
        
        # Añadir dos supervivientes a la partida
        partida.supervivientes.add(superviviente1, superviviente2)
        
        # Verificar que la partida tiene dos supervivientes
        self.assertEqual(partida.supervivientes.count(), 2)
        
    
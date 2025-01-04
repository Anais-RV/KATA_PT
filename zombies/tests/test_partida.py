from django.test import TestCase
from django.core.exceptions import ValidationError
from zombies.models import Partida, Superviviente

class PartidaTestCase(TestCase):
    def test_partida_comienza_sin_supervivientes(self):
        """Test para verificar que una partida comienza con 0 supervivientes."""
        partida = Partida.objects.create(jugador="Jugador 1")  
        self.assertEqual(partida.supervivientes.count(), 0)

    def test_añadir_supervivientes_a_partida(self):
        """Test para verificar que una partida puede tener supervivientes."""
        partida = Partida.objects.create(jugador="Jugador 1")
        
        # Crear supervivientes
        superviviente1 = Superviviente.objects.create(nombre="Superviviente 1")
        superviviente2 = Superviviente.objects.create(nombre="Superviviente 2")
        
        # Añadir dos supervivientes a la partida
        partida.supervivientes.add(superviviente1, superviviente2)
        
        # Verificar que la partida tiene dos supervivientes
        self.assertEqual(partida.supervivientes.count(), 2)
        
    def test_nombres_supervivientes_únicos_en_partida(self):
        """Test para verificar que los nombres de los supervivientes en una partida son únicos."""
        
        # Crear una partida
        partida = Partida.objects.create(jugador="Jugador 1")
        
        # Crear un superviviente
        superviviente1 = Superviviente.objects.create(nombre="Superviviente 1")
        partida.supervivientes.add(superviviente1)
        
        # Intentar crear otro superviviente con el mismo nombre
        superviviente2 = Superviviente.objects.create(nombre="Superviviente 1")
        with self.assertRaises(ValidationError):
            partida.supervivientes.add(superviviente2)

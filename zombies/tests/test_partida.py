from django.test import TestCase
from django.core.exceptions import ValidationError
from zombies.models import Partida, Superviviente
from django.db import IntegrityError

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
        with self.assertRaises(IntegrityError):
            superviviente2 = Superviviente.objects.create(nombre="Superviviente 1")


    def test_partida_finaliza_si_supervivientes_muertos(self):
        """Test para verificar que una partida finaliza si todos los supervivientes están muertos."""

        # Crear una partida
        partida = Partida.objects.create(jugador="Jugador 1")
        superviviente1 = Superviviente.objects.create(nombre="Superviviente 1", vivo=True)
        superviviente2 = Superviviente.objects.create(nombre="Superviviente 2", vivo=True)
        partida.supervivientes.add(superviviente1, superviviente2)

        # Verificar que la partida no ha finalizado
        self.assertFalse(partida.finalizada)

        # Marcar a los supervivientes como muertos
        superviviente1.heridas = 2
        superviviente1.save()
        superviviente2.heridas = 2
        superviviente2.save()

        # Verificar que la partida ha finalizado automáticamente
        partida.refresh_from_db()
        self.assertTrue(partida.finalizada)

        
        
       
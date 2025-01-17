from django.test import TestCase
from zombies.models import Partida, Superviviente

class Niveles(TestCase):
    def test_superviviente_gana_experiencia_sube_nivel(self):
        """Test que verifica que un superviviente sube de nivel al ganar suficiente experiencia."""
        
        superviviente = Superviviente.objects.create(nombre="Superviviente 1", experiencia=0, nivel="Azul")
        
        # Subir a nivel Amarillo
        superviviente.experiencia = 7
        superviviente.save()
        self.assertEqual(superviviente.nivel, "Amarillo")
        
        # Subir a nivel Naranja
        superviviente.experiencia = 19
        superviviente.save()
        self.assertEqual(superviviente.nivel, "Naranja")
        
        # Subir a nivel Rojo
        superviviente.experiencia = 43
        superviviente.save()
        self.assertEqual(superviviente.nivel, "Rojo")   
    
class PartidaNivelTestCase(TestCase):
    def test_actualizar_nivel_partida(self):
        """Test para verificar que el nivel de la partida se actualiza según los supervivientes vivos."""
        partida = Partida.objects.create(jugador="Jugador 1")
        sup1 = Superviviente.objects.create(nombre="Superviviente 1", nivel='Azul', vivo=True)
        sup2 = Superviviente.objects.create(nombre="Superviviente 2", nivel='Naranja', vivo=True)
        partida.supervivientes.add(sup1, sup2)

        partida.actualizar_nivel()
        self.assertEqual(partida.nivel, 'Naranja')

        sup2.vivo = False
        sup2.save()
        partida.actualizar_nivel()
        self.assertEqual(partida.nivel, 'Azul')
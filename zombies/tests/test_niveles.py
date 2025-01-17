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
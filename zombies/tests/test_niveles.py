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
    
    def test_actualizar_nivel_partida(self):
        """Test para verificar que el nivel de la partida se actualiza según los supervivientes vivos."""
        partida = Partida.objects.create(jugador="Jugador 1")

        # Crear supervivientes
        sup1 = Superviviente.objects.create(nombre="Superviviente 1", experiencia=0)  # Nivel Azul
        sup2 = Superviviente.objects.create(nombre="Superviviente 2", experiencia=19)  # Nivel Naranja

        # Añadir supervivientes a la partida
        partida.supervivientes.add(sup1, sup2)

        # Verificar nivel inicial
        partida.actualizar_nivel()
        self.assertEqual(partida.nivel, 'Naranja')  # Nivel más alto debería ser 'Naranja'

        # Cambiar el estado de sup2 a muerto
        sup2.heridas = 2  # Marca a sup2 como muerto
        sup2.save()  # Esto actualizará el estado de vivo

        # Refrescar las instancias
        sup2.refresh_from_db()
        partida.refresh_from_db()

        # Actualizar nivel de la partida
        partida.actualizar_nivel()
        print(f"Nivel de la partida después de actualizar: {partida.nivel}")
        self.assertEqual(partida.nivel, 'Azul')  # Solo queda sup1 con nivel Azul





    
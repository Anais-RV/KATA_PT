from django.test import TestCase
from zombies.models import Equipo, Superviviente

class EquipoTestCase(TestCase):

    def test_crear_equipo_asignado_a_superviviente(self):
        
        """ Test para crear un equipo y asignarlo a un superviviente """

        # Creamos un superviviente con un nombre
        superviviente = Superviviente.objects.create(nombre="Arancha")

        # Creamos un equipo asignado al superviviente
        equipo = Equipo(nombre="Hacha", tipo="Mano", superviviente=superviviente)

        # Verificamos que el equipo ha sido asignado correctamente
        self.assertEqual(equipo.nombre, "Hacha")
        self.assertEqual(equipo.tipo, "Mano")
        self.assertEqual(equipo.superviviente, superviviente)
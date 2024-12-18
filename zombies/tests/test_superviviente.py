from django.test import TestCase
from zombies.models import Superviviente

class SupervivienteTestCase(TestCase):
    def test_crear_superviviente(self):

        """ Test para crear un superviviente e inicializarlo correctamente """

        # Creamos un superviviente con un nombre
        superviviente = Superviviente(nombre="Arancha")

        # Verificamos valores iniciales
        self.assertEqual(superviviente.nombre, "Arancha")
        self.assertEqual(superviviente.heridas, 0)
        self.assertEqual(superviviente.acciones, 3)
        self.assertEqual(superviviente.experiencia, 0)
        self.assertEqual(superviviente.nivel, "Azul")


    def test_superviviente_muere_con_dos_heridas(self):

        """ Test para verificar que el superviviente muere si recibe 2 heridas """

        # Creamos un superviviente con un nombre
        superviviente = Superviviente(nombre="Arancha")

        # Añadir 2 heridas
        superviviente.heridas = 2

        # Verificar que el superviviente ha muerto
        self.assertTrue(superviviente.esta_muerto())
    
    def test_superviviente_tiene_tres_acciones_por_turno(self):

        """ Test para verificar que el superviviente tiene 3 acciones por turno """

        # Creamos un superviviente con un nombre
        superviviente = Superviviente(nombre="Arancha")

        # Verificar que el superviviente tiene 3 acciones
        self.assertEqual(superviviente.acciones, 3)
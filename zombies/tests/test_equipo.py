from django.core.exceptions import ValidationError
from django.test import TestCase
from zombies.models import Equipo, Superviviente

class EquipoTestCase(TestCase):

    def test_crear_equipo_asignado_a_superviviente(self):
        """ Test para crear un equipo y asignarlo a un superviviente """
        superviviente = Superviviente.objects.create(nombre="Arancha")
        equipo = Equipo(nombre="Hacha", tipo="Mano", superviviente=superviviente)
        self.assertEqual(equipo.nombre, "Hacha")
        self.assertEqual(equipo.tipo, "Mano")
        self.assertEqual(equipo.superviviente, superviviente)

    def test_superviviente_lleva_hasta_5_piezas_equipo(self):

        """Test para verificar que un superviviente puede llevar como max 5 piezas de equipo """

        # Creamos un superviviente
        superviviente = Superviviente.objects.create(nombre="Arancha")

        # Creamos 5 piezas de equipo
        for i in range(1, 6):
            Equipo.objects.create(nombre=f"Equipo_{i}", tipo="Reserva", superviviente=superviviente)

        # Tratamos de agregar una sexta pieza directamente en la lógica de validación
        with self.assertRaises(ValidationError):
            Equipo.objects.create(nombre="Molotov", tipo="Reserva", superviviente=superviviente)

        # Verificamos que el superviviente aún tiene solo 5 piezas
        self.assertEqual(superviviente.equipo.count(), 5)

    def test_distribuir_equipo_en_mano_y_reserva(self):
        
        """Test para verificar que las piezas de equipo se distribuyen entre 'En Mano' y 'En Reserva'."""

        # Creamos un superviviente
        superviviente = Superviviente.objects.create(nombre="Arancha")

        # Creamos 3 piezas de equipo, intentando asignar 3 "En Mano"
        Equipo.objects.create(nombre="Bate", tipo="Mano", superviviente=superviviente)
        Equipo.objects.create(nombre="Katana", tipo="Mano", superviviente=superviviente)
        
        with self.assertRaises(ValueError):  # Verificamos que se lanza un error
            Equipo.objects.create(nombre="Pistola", tipo="Mano", superviviente=superviviente)

        # Creamos una pieza adicional "En Reserva"
        Equipo.objects.create(nombre="Molotov", tipo="Reserva", superviviente=superviviente)

        # Verificamos que el superviviente tiene exactamente 2 piezas "En Mano" y 1 en "Reserva"
        self.assertEqual(superviviente.equipo.filter(tipo="Mano").count(), 2)
        self.assertEqual(superviviente.equipo.filter(tipo="Reserva").count(), 1)



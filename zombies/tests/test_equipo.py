from django.core.exceptions import ValidationError
from django.test import TestCase
from zombies.models import Equipo, Superviviente

class EquipoTestCase(TestCase):

    def setUp(self):
        """Test para crear un Superviviente para las pruebas."""
        self.superviviente = Superviviente.objects.create(nombre="Arancha")

    def test_crear_equipo_asignado_a_superviviente(self):
        """Test para crear un equipo y asignarlo a un superviviente."""
        equipo = Equipo.objects.create(nombre="Hacha", tipo="Mano", superviviente=self.superviviente)
        self.assertEqual(equipo.nombre, "Hacha")
        self.assertEqual(equipo.tipo, "Mano")
        self.assertEqual(equipo.superviviente, self.superviviente)

    def test_superviviente_lleva_hasta_5_piezas_equipo(self):
        """Test para verificar que un superviviente puede llevar como máximo 5 piezas de equipo."""
        for i in range(5):
            Equipo.objects.create(nombre=f"Equipo_{i}", tipo="Reserva", superviviente=self.superviviente)

        with self.assertRaises(ValidationError):
            Equipo.objects.create(nombre="Molotov", tipo="Reserva", superviviente=self.superviviente)

        self.assertEqual(self.superviviente.equipo.count(), 5)

    def test_distribuir_equipo_en_mano_y_reserva(self):
        """Test para verificar que las piezas de equipo se distribuyen entre 'En Mano' y 'En Reserva'."""
        Equipo.objects.create(nombre="Bate", tipo="Mano", superviviente=self.superviviente)
        Equipo.objects.create(nombre="Katana", tipo="Mano", superviviente=self.superviviente)

        with self.assertRaises(ValidationError):
            Equipo.objects.create(nombre="Pistola", tipo="Mano", superviviente=self.superviviente)

        Equipo.objects.create(nombre="Molotov", tipo="Reserva", superviviente=self.superviviente)

        self.assertEqual(self.superviviente.equipo.filter(tipo="Mano").count(), 2)
        self.assertEqual(self.superviviente.equipo.filter(tipo="Reserva").count(), 1)

    def test_reducir_capacidad_por_heridas(self):
        """Test para verificar que la capacidad de equipo se reduce por heridas."""
        for i in range(5):
            Equipo.objects.create(nombre=f"Equipo_{i}", tipo="Reserva", superviviente=self.superviviente)

        self.superviviente.heridas = 1
        self.superviviente.save()

        self.assertEqual(self.superviviente.equipo.count(), 4)
        self.assertEqual(self.superviviente.equipo.filter(tipo="Reserva").count(), 4)

    def test_limite_cinco_piezas_con_eliminacion(self):
        """Test para verificar que al superar el límite, se elimina la pieza correcta."""
        for i in range(5):
            Equipo.objects.create(nombre=f"Equipo_{i}", tipo="Reserva", superviviente=self.superviviente)

        self.superviviente.heridas = 1
        self.superviviente.save()

        self.assertEqual(self.superviviente.equipo.count(), 4)
        piezas_restantes = self.superviviente.equipo.all().values_list('nombre', flat=True)
        self.assertNotIn("Equipo_0", piezas_restantes)

    def test_equipo_tipo_invalido(self):
        """Test para verificar que se lanza un error si el tipo de equipo no es válido."""
        with self.assertRaises(ValidationError):
            Equipo.objects.create(nombre="Equipo_Inválido", tipo="Invalido", superviviente=self.superviviente)

    def test_limite_piezas_con_multiples_supervivientes(self):
        """Test para verificar que los límites de equipo funcionan con múltiples supervivientes."""
        superviviente2 = Superviviente.objects.create(nombre="Juan")

        for i in range(5):
            Equipo.objects.create(nombre=f"Equipo_Arancha_{i}", tipo="Reserva", superviviente=self.superviviente)

        Equipo.objects.create(nombre="Espada", tipo="Mano", superviviente=superviviente2)

        self.assertEqual(self.superviviente.equipo.count(), 5)
        self.assertEqual(superviviente2.equipo.count(), 1)

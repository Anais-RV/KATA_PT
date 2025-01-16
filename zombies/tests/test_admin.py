from django.test import TestCase
from django.contrib.admin.sites import site
from zombies.models import Partida

class PartidaAdminTestCase(TestCase):
    def test_partida_admin_muestra_campos_correctos(self):
        """Test para verificar que el admin de Partida muestra los campos esperados."""
        # Obtén la configuración del admin para Partida
        admin_config = site._registry[Partida]

        # Verifica los campos en list_display
        campos_esperados = ['jugador', 'supervivientes_count']
        for campo in campos_esperados:
            with self.subTest(campo=campo):
                self.assertIn(campo, admin_config.list_display)

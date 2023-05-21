from django.test import TestCase
from django.db.transaction import TransactionManagementError

from Basquet1.models import Clubes

class ClubesTest(TestCase):
    # PRUEBAS PARA CLUBES
    def test_creacion_clubes_1(self):
        # uso esperado
        club = Clubes.objects.create(nombre="Titulo", fecha_de_fundacion="1990-12-12", categoria_juego="Liga Nacional")
        club.save()

        self.assertEqual(Clubes.objects.count(), 1)
        self.assertIsNotNone(club.id)

    def test_creacion_clubes_2(self):
        # uso esperado
        with self.assertRaises(TransactionManagementError), self.assertRaises(ValueError):
            club = Clubes.objects.create(nombre="Titulo", fecha_de_fundacion="lopez", categoria_juego="SERIAL-1")
            club.save()
        
        self.assertEqual(Clubes.objects.count(), 0)








from django.test import TestCase
from WebShop.trgovina.views.narudzbe import OrderView


class Testmodels(TestCase):

    def setUp(self):
        self.order1 = OrderView.objects.create(
            proizvod = 'some-comic',
            kupac = 'some-name',
            kolicina = '1',
            cijena = '30',
            adresa = 'TestAdress',
            telefon = '098453354',
            datum = 'TestDate',
            status = 'active'
        )

    def test_order(self):
        self.assertEquals(self.order1.kupac_id, "narudzba")
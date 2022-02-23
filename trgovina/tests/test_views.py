from django.test import TestCase, Client
from django.urls import reverse
from WebShop.trgovina.views.narudzbe import OrderView

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.narudzbe_q_url = reverse('narudzba')

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

    def test_project_narudzbe_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'narudzbe.html')

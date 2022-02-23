from django.test import SimpleTestCase
from django.urls import reverse, resolve
from trgovina.views.home import Index
from trgovina.views.cart import Kosarica
from trgovina.views.narudzbe import OrderView



class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('homepage')

        self.assertEquals(resolve(url).func.view_class, Index)


    def test_kosarica_url_is_resolved(self):
        url = reverse('Kosarica')

        self.assertEquals(resolve(url).func.view_class, Kosarica)

    def test_order_view_url_is_resolved(self):
        url = reverse('Narudzbe')

        self.assertEquals(resolve(url).func.view_class, OrderView)


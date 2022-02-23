from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from trgovina.models import Kupac
from trgovina.models import Proizvodi
from django.views import  View

class Kosarica(View):
    def get(self , request):
        ids = list(request.session.get('kosarica').keys())
        proizvodi = Proizvodi.get_products_by_id(ids)
        print(proizvodi)
        return render(request , 'kosarica.html' , {'proizvodi' : proizvodi} )
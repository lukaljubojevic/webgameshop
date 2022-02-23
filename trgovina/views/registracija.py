from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from trgovina.models import Kupac
from django.views import View
  
  
class Signup (View):
    def get(self, request):
        return render(request, 'registracija.html')
  
    def post(self, request):
        postData = request.POST
        ime = postData.get('ime')
        prezime = postData.get('prezime')
        telefon = postData.get('telefon')
        email = postData.get('email')
        lozinka = postData.get('lozinka')
        # validation
        value = {
            'ime': ime,
            'prezime': prezime,
            'telefon': telefon,
            'email': email
        }
        error_message = None
  
        kupac = Kupac(ime=ime,
                            prezime=prezime,
                            telefon=telefon,
                            email=email,
                            lozinka=lozinka)
        error_message = self.validateKupac(kupac)
  
        if not error_message:
            print(ime,prezime,telefon,email,lozinka)
            kupac.lozinka = make_password(kupac.lozinka)
            kupac.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'registracija.html', data)
  
    def validateKupac(self, kupac):
        error_message = None
        if (not kupac.ime):
            error_message = "Morate unesti ime!"
        elif not kupac.prezime:
            error_message = 'Morate unesti prezime'
        elif not kupac.telefon:
            error_message = 'Molim Vas telefon'
        elif len(kupac.lozinka) < 4:
            error_message = 'Lozinka mora imati 4+ znakova'
        elif kupac.isExists():
            error_message = 'Vec ste registrirani'
        return error_message
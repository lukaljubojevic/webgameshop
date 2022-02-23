from django.shortcuts import render, redirect, HttpResponseRedirect
from trgovina.models import Proizvodi
from trgovina.models import Kategorija
from django.views import View

class Index(View):
    def post(self, request):
        proizvodi = request.POST.get('p')
        brisanje = request.POST.get('remove')
        kosarica = request.session.get('kosarica')
        if kosarica:
            kolicina = kosarica.get(proizvodi)
            if kolicina:
                if brisanje:
                    if kolicina <= 1:
                        kosarica.pop(proizvodi)
                    else:
                        kosarica[proizvodi] = kolicina-1
                else:
                    kosarica[proizvodi] = kolicina+1
  
            else:
                kosarica[proizvodi] = 1
        else:
            kosarica = {}
            kosarica[proizvodi] = 1
  
        request.session['kosarica'] = kosarica
        return redirect('homepage')
  
    def get(self, request):
        return HttpResponseRedirect(f'/trgovina{request.get_full_path()[1:]}')
  
  
def trgovina(request):
    kosarica = request.session.get('kosarica')
    if not kosarica:
        request.session['kosarica'] = {}
    proizvodi = None
    kategorija = Kategorija.get_all_categories()
    kategorijaID = request.GET.get('kategorija')
    if kategorijaID:
        proizvodi = Proizvodi.get_all_products_by_categoryid(kategorijaID)
    else:
        proizvodi = Proizvodi.get_all_products()
  
    data = {}
    data['proizvodi'] = proizvodi
    data['kategorija'] = kategorija
    return render(request, 'index.html', data)
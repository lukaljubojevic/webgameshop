from django.db import models
import datetime
# Create your models here.
class Kategorija (models.Model):
    naziv=models.CharField(max_length=50)
    @staticmethod
    def get_all_categories():
        return Kategorija.objects.all()
    
    def __str__(self):
        return self.naziv

class Kupac(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    telefon = models.CharField(max_length=10)
    email = models.EmailField()
    lozinka = models.CharField(max_length=100)
  
    # to save the data
    def register(self):
        self.save()
  
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Kupac.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if Kupac.objects.filter(email=self.email):
            return True
  
        return False

class Proizvodi(models.Model):
    id=models.IntegerField(primary_key=True, db_column='id')
    naziv = models.CharField(max_length=60)
    cijena = models.IntegerField(default=0)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE, default=1)
    opis = models.CharField(
        max_length=250, default='', blank=True, null=True)
    slika = models.ImageField(upload_to='uploads/proizvodi/')
  
    @staticmethod
    def get_products_by_id(ids):
        return Proizvodi.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Proizvodi.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(kategorija_id):
        if kategorija_id:
            return Proizvodi.objects.filter(kategorija=kategorija_id)
        else:
            return Proizvodi.get_all_products()

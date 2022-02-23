from django.contrib import admin
from .models import *


class AdminProizvod(admin.ModelAdmin):
    list_display = ['naziv', 'cijena', 'kategorija']


class KategorijaAdmin(admin.ModelAdmin):
    list_display = ['naziv']

# Register your models here.
admin.site.register(Proizvodi,AdminProizvod)
admin.site.register(Kategorija)
admin.site.register(Kupac)

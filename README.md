# Uvod: 
Ova aplikacija biti će web trgovina s prikazom artikala po kategorijama: igrice, stripovi, figurice (eng. "movie/comic props") bez mogućnosti kupnje, ali biti će moguće dodati artikl u košaricu.

Od prethodno predanog tutorijala i modela smo odustali pa je sve izrađeno ponovno uz drugi.

# Funkcionalnosti
1) Pregled kategorija
2) Prikaz svih proizvoda po kategoriji
3) Prikaz detalja o proizvodu iz kategorije
4) Dodavanje proizvoda u košaricu
5) Administriranje sustava pomoću admin panela
6) Dodavanje korisnika (koristiti će se gotov Django User model i forma)

# Model  
Model se sastoji od:
1. Kategorije - definira naziv kategorije proizvoda (strip, videoigra, figurica,...) i metodu koja vraća sve objekte unutar neke kategorije
2. Kupca - model kupca se sastoji od atributa: ime, prezime, telefon, mail i lozinka
    * Uz to definirane su i dvije metode: dohvati kupca po email adresi i postoji li kupac u bazi
4. Proizvoda - model proizvoda prikazuje id, naziv, cijenu, opis, sliku i kategoriju kojoj pripada nekog proizvoda.
    * Uz to definirane su i tri metode: dohvati prozivode po ID-u, dohvati sve proizvode i dohvati sve proizvode po kategoriji

# Dodatne informacije: 
Košarica je realizirana kao objekt unutar sesije od prijavljenog korisnika (views/home.py - metoda trgovina), a proizvodi se u košaricu dodaju metodom post (views/home.py).

Pogled košarica (views/kosarica.py) dohvaća košaricu za korisničku sesiju i dohvaća sve proizvode dodane u košaricu za tu sesiju.


Tutorijal korišten za izradu aplikacije:
```
https://github.com/TanuShree952838/Eshop
Materijali s vježbi PW
```

from django import template

register = template.Library ()


@register.filter (name='je_u_kosarici')
def je_u_kosarici(proizvodi, kosarica):
    keys = kosarica.keys()
    for i in keys:
        if  i == proizvodi.id:
            return True
    return False;


@register.filter (name='kosarica_kolicina')
def kosarica_kolicina(proizvodi, kosarica):
    keys = kosarica.keys()
    for id in keys:
        if int (id) == int(proizvodi.id):
            return kosarica.get (id)
    return 0;


@register.filter (name='ukupna_cijena')
def ukupna_cijena(proizvodi, kosarica):
    return proizvodi.cijena * kosarica_kolicina(proizvodi, kosarica)

@register.filter (name='cijena_kosarice')
def cijena_kosarice(proizvodi, kosarica):
    suma = 0;
    for p in proizvodi:
        suma += ukupna_cijena(p, kosarica)
    return suma
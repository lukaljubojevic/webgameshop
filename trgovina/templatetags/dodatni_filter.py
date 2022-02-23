from django import template
register = template.Library()

@register.filter(name='valuta')
def valuta(number):
    return str(number) + " HRK"

@register.filter(name='mnozenje')
def mnozenje(a , b):
    return a * b
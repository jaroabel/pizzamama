from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza


# Create your views here.
# Les pizzas : Végétarienne, Poulet champignons, 4 fromages, Carnivore
# / menu
def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_name_and_price = [pizza.nom + " : " + str(pizza.prix) + "$" for pizza in pizzas]

    pizzas_name_and_price_str = ", ".join(pizzas_name_and_price)
    return HttpResponse("Les pizzas : " + pizzas_name_and_price_str)'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})

def api_get_pizzas(reguest):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)

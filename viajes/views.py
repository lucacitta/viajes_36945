from django.shortcuts import render

from viajes.models import Viaje, Destino

def listar_viajes(request):
    lista_viajes = Viaje.objects.all()
    context = {'lista_viajes':lista_viajes}
    return render(request, 'lista_viajes.html', context=context)

def listar_destinos(request):
    listar_destinos = Destino.objects.all()
    context = {'listar_destinos':listar_destinos}
    return render(request, 'listar_destinos.html', context=context)
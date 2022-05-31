from django.shortcuts import render

from viajes.models import Viaje

def listar_viajes(request):
    lista_viajes = Viaje.objects.all()
    context = {'lista_viajes':lista_viajes}
    return render(request, 'lista_viajes.html', context=context)
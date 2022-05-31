from django.urls import path

from viajes.views import listar_destinos, listar_viajes


urlpatterns = [
    path('', listar_viajes, name = 'lista_viajes'),
    path('destinos/', listar_destinos, name='listar_destinos')
]


from django.urls import path

from viajes.views import listar_viajes


urlpatterns = [
    path('', listar_viajes, name = 'lista_viajes')
]

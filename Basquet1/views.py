from django.shortcuts import render
from Basquet1.models import Entrenadores, Clubes, Jugadores
def listar_jugadores(request):
    contexto = {
         "jugadores": Jugadores.objects.all(),
    }

    http_response = render(
        request=request,
        template_name='Basquet1/lista_jugadores.html',
        context= contexto 
    )
    return http_response

def listar_entrenadores(request):
    contexto = {
         "entrenadores": Entrenadores.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Basquet1/lista_entrenadores.html',
        context= contexto 
    )
    return http_response
def listar_clubes(request):
    contexto = {
         "clubes": Clubes.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Basquet1/lista_clubes.html',
        context= contexto 
    )
    return http_response

def crear_club(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='Basquet1/formulario_basquet_1.html',
        context= contexto 
    )
    return http_response



from django.shortcuts import render, redirect
from django.urls import reverse
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

def cargar_club(request):
    if request.method == "POST":
        data = request.POST
        nombre_club= data["nombre"]
        categoria_maxima = data["categoria"]
        fecha_de_fundacion = data["fecha_fundacion"]
        club = Clubes(nombre=nombre_club, categoria_juego= categoria_maxima, fecha_fundacion=fecha_de_fundacion)
        club.save()
        url_exitosa = reverse('clubes')
        return redirect(url_exitosa)
    else: 
        http_response = render(
        request=request,
        template_name='Basquet1/formulario_basquet_1.html',
    )
    return http_response



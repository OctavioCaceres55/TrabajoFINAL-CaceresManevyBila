from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludar_con_html(request):
    contexto = {
        "Jugador": "Facundo Campazzo",
    } 
    http_response = render(
        request=request,
        template_name='Basquet1/basquet.html',
        context=contexto 
    )
    return http_response
def saludar_con_html_1(request):
    contexto = {} 
    http_response = render(
        request=request,
        template_name='Basquet1/base.html',
        context=contexto 
    )
    return http_response

def inicio(request): 
    contexto = {}
    http_response = render(
        request=request,
        template_name='Basquet1/index.html',
        context= contexto 
    )
    return http_response



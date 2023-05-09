from django.shortcuts import render

def listar_jugadores(request):
    contexto = {
         "jugadores": [
            {"nombre" : "Facundo", "apellido" : "Campazzo"},
            {"nombre" : "Luca", "apellido" : "Vildoza"},
            {"nombre" : "Felipe", "apellido" : "Pais"},
        ]
    }
    http_response = render(
        request=request,
        template_name='Basquet1/lista_jugadores.html',
        context= contexto 
    )
    return http_response

def listar_entrenadores(request):
    contexto = {
         "entrenadores": [
            {"nombre" : "Julio", "apellido" : "Lamas"},
            {"nombre" : "Gregg", "apellido" : "Poppovich"},
            {"nombre" : "Marcelo", "apellido" : "Cirillo"},
        ]
    }
    http_response = render(
        request=request,
        template_name='Basquet1/lista_entrenadores.html',
        context= contexto 
    )
    return http_response


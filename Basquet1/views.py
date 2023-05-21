from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from Basquet1.models import Entrenadores, Clubes, Jugadores
from Basquet1.forms import EntrenadoresFormulario
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Vistas Entrenadores

def listar_entrenadores(request):

    contexto = {
         "entrenadores": Entrenadores.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Basquet1/panel_entrenadores.html',
        context= contexto 
    )
    return http_response

def buscar_entrenadores(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        print(f"Usted buscó {busqueda}")
        entrenadores = Entrenadores.objects.filter(apellido__contains=busqueda)
        contexto = {
            "entrenadores": entrenadores
    }
        
    http_response = render(
        request=request,
        template_name='Basquet1/panel_entrenadores.html',
        context= contexto,
    )
    return http_response

@login_required
def cargar_entrenador(request):
    if request.method == "POST":
        formulario = EntrenadoresFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido =data["apellido"]
            lugar_de_nacimiento = data["lugar_de_nacimiento"]
            fecha_de_nacimiento = data["fecha_de_nacimiento"]
            trayectoria = data["trayectoria"]
            creador = request.user
            entrenador = Entrenadores(nombre=nombre, apellido=apellido, lugar_de_nacimiento=lugar_de_nacimiento, fecha_de_nacimiento=fecha_de_nacimiento,trayectoria=trayectoria, creador = creador)
            entrenador.save()        
            url_exitosa = reverse('entrenadores')
            return redirect(url_exitosa)
              
    else: 
        formulario = EntrenadoresFormulario()    
    http_response = render(
        request=request,
        template_name='Basquet1/formulario_entrenadores.html',
        context={'formulario': formulario},
    )
    return http_response

@login_required
def eliminar_entrenador(request, id):
   curso = Entrenadores.objects.get(id=id)
   if request.method == "POST":
       curso.delete()
       url_exitosa = reverse('entrenadores')
       return redirect(url_exitosa)
   
@login_required
def editar_entrenador(request, id):
   entrenador = Entrenadores.objects.get(id=id)
   if request.method == "POST":
       formulario = EntrenadoresFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           entrenador.nombre = data['nombre']
           entrenador.apellido = data['apellido']
           entrenador.fecha_de_nacimiento = data['fecha_de_nacimiento']
           entrenador.lugar_de_nacimiento = data['lugar_de_nacimiento']
           entrenador.trayectoria = data['trayectoria']
           entrenador.save()
           url_exitosa = reverse('entrenadores')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': entrenador.nombre,
           'apellido': entrenador.apellido,
           'fecha_de_nacimiento': entrenador.fecha_de_nacimiento, 
           'lugar_de_nacimiento': entrenador.lugar_de_nacimiento,
           'Trayectoria': entrenador.trayectoria,
       }
       formulario = EntrenadoresFormulario(initial=inicial)
   return render(
       request=request,
       template_name='Basquet1/formulario_entrenadores.html',
       context={'formulario': formulario},
   )

# Vistas Jugadores

class JugadoresListView(ListView):
    model = Jugadores
    template_name = 'Basquet1/panel_jugadores.html'

class JugadoresDetailView(LoginRequiredMixin ,DeleteView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')

class JugadoresCreateView(LoginRequiredMixin, CreateView):
    model = Jugadores
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'esta_habilitado')
    success_url = reverse_lazy('listar_jugadores')

class JugadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')

class JugadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Jugadores
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento')
    success_url = reverse_lazy('listar_jugadores')

# Vistas Clubes

def listar_clubes(request):
    contexto = {
         "clubes": Clubes.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Basquet1/panel_clubes.html',
        context= contexto 
    )
    return http_response

@login_required
def cargar_club(request):
    if request.method == "POST":
        data = request.POST
        nombre_club= data["nombre"]
        categoria_maxima = data["categoria"]
        fecha_de_fundacion = data["fecha_fundacion"]
        creador = request.user
        club = Clubes(nombre=nombre_club, categoria_juego= categoria_maxima, fecha_fundacion=fecha_de_fundacion, creador=creador)
        club.save()
        url_exitosa = reverse('clubes')
        return redirect(url_exitosa)
    else: 
        http_response = render(
        request=request,
        template_name='Basquet1/formulario_clubes.html',
    )
    return http_response


def buscar_clubes(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        print(f"Usted buscó {busqueda}")
        print(busqueda)
        clubes = Clubes.objects.filter(categoria_juego=busqueda)
        contexto = {
            "clubes": clubes
        }

    http_response = render(
        request=request,
        template_name='Basquet1/panel_clubes.html',
        context= contexto,
    )
    return http_response
 
@login_required
def eliminar_club(request, id):
   curso = Clubes.objects.get(id=id)
   if request.method == "POST":
       curso.delete()
       url_exitosa = reverse('clubes')
       return redirect(url_exitosa)
   


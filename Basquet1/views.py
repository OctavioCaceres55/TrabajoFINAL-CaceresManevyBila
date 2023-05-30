from typing import Any
from django.http import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from Basquet1.models import Entrenadores, Clubes, Jugadores, Aboutme, Articulo
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, redirect
from Basquet1.forms import ArticuloFormulario
# Vistas Entrenadores

class EntrenadoresListView(ListView):
    model = Entrenadores
    template_name = 'Basquet1/panel_entrenadores.html'
    context_object_name = 'entrenadores'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('p')
        if query:
            queryset = queryset.filter(apellido__icontains=query)
        return queryset

class EntrenadoresDetailView(DetailView):
    model = Entrenadores
    success_url = reverse_lazy('listar_entrenadores')

class EntrenadoresCreateView(LoginRequiredMixin, CreateView):
    model = Entrenadores
    fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'trayectoria', 'creador1']
    success_url = reverse_lazy('listar_entrenadores')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EntrenadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Entrenadores
    success_url = reverse_lazy('listar_entrenadores')

class EntrenadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Entrenadores
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'trayectoria', 'creador1')
    success_url = reverse_lazy('listar_entrenadores')

# Vistas Jugadores

class JugadoresListView(ListView):
    model = Jugadores
    template_name = 'Basquet1/panel_jugadores.html'
    context_object_name = 'jugadores'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('p')
        if query:
            queryset = queryset.filter(apellido__icontains=query)
        return queryset


class JugadoresDetailView(DetailView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')

class JugadoresCreateView(LoginRequiredMixin, CreateView):
    model = Jugadores
    fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'esta_habilitado', 'numero_camiseta','club', 'creador1']
    success_url = reverse_lazy('listar_jugadores')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JugadoresDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')
    template_name = 'Basquet1/jugadores_confirm_delete.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

class JugadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Jugadores
    fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'esta_habilitado', 'numero_camiseta','club', 'creador1']
    success_url = reverse_lazy('listar_jugadores')

# Vistas Clubes
class ClubesListView(ListView):
    model = Clubes
    template_name = 'Basquet1/panel_clubes.html'
    context_object_name = 'clubes'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('w')
        if query:
            queryset = queryset.filter(categoria_juego__icontains=query)
        return queryset

class ClubesDetailView(DetailView):
    model = Clubes
    success_url = reverse_lazy('listar_clubes')

class ClubesCreateView(LoginRequiredMixin, CreateView):
    model = Clubes
    fields = ['nombre', 'categoria_juego', 'fecha_fundacion', 'creador1']
    success_url = reverse_lazy('listar_clubes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ClubesDeleteView(LoginRequiredMixin, DeleteView):
    model = Clubes
    success_url = reverse_lazy('listar_clubes')

class ClubesUpdateView(LoginRequiredMixin, UpdateView):
    model = Clubes
    fields = ('nombre', 'fecha_fundacion', 'categoria_juego', 'creador1')
    success_url = reverse_lazy('listar_clubes')


# VIEWS ABOUT ME

class AboutmeListView(ListView):
    model = Aboutme
    template_name= 'Basquet1/about_me.html'

class AboutmeDetailView(DetailView):
    model = Aboutme
    success_url = reverse_lazy('detalles')

class AboutmeCreateView(CreateView):
    model = Aboutme
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'biografia')
    success_url = reverse_lazy('detalles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AboutmeUpdateView(UpdateView):
    model = Aboutme
    success_url = reverse_lazy('detalles')

# VIEWS ARTICULOS
        
def listar_articulos(request):
   contexto = {
       "articulos": Articulo.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='Basquet1/listar_articulos.html',
       context=contexto,
   )
   return http_response


def buscar_articulo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        articulos = Articulo.objects.filter(titulo__contains=busqueda)
        contexto = {
            "articulos": articulos,
            "reciente": busqueda
        }
        http_response = render(
            request=request,
            template_name='Basquet1/listar_articulos.html',
            context=contexto,
        )
        return http_response
    
class ArticuloCreateView(CreateView, LoginRequiredMixin):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo','autor', 'fecha')
    success_url = reverse_lazy('listar_articulo')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('listar_articulo')

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo','autor', 'fecha')
    success_url = reverse_lazy('listar_articulo')

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('listar_articulo')  



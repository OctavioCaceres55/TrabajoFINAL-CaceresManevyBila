from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from Basquet1.models import Entrenadores, Clubes, Jugadores, Articulos
from Basquet1.forms import EntrenadoresFormulario
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Vistas Entrenadores

class EntrenadoresListView(ListView):
    model = Entrenadores
    template_name = 'Basquet1/panel_entrenadores.html'

class EntrenadoresDetailView(DetailView):
    model = Entrenadores
    success_url = reverse_lazy('listar_entrenadores')

class EntrenadoresCreateView(LoginRequiredMixin, CreateView):
    model = Entrenadores
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'trayectoria', 'imagen')
    success_url = reverse_lazy('listar_entrenadores')

class EntrenadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Entrenadores
    success_url = reverse_lazy('listar_entrenadores')

class EntrenadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Entrenadores
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'trayectoria', 'imagen')
    success_url = reverse_lazy('listar_entrenadores')

# Vistas Jugadores

class JugadoresListView(ListView):
    model = Jugadores
    template_name = 'Basquet1/panel_jugadores.html'

class JugadoresDetailView(DetailView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')

class JugadoresCreateView(LoginRequiredMixin, CreateView):
    model = Jugadores
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'esta_habilitado','imagen')
    success_url = reverse_lazy('listar_jugadores')

class JugadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')

class JugadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Jugadores
    fields = ('apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'imagen')
    success_url = reverse_lazy('listar_jugadores')

# Vistas Clubes
class ClubesListView(ListView):
    model = Clubes
    template_name = 'Basquet1/panel_clubes.html'

class ClubesDetailView(DetailView):
    model = Clubes
    success_url = reverse_lazy('listar_clubes')

class ClubesCreateView(LoginRequiredMixin, CreateView):
    model = Clubes
    fields = ('nombre', 'categoria_juego', 'fecha_fundacion','imagen')
    success_url = reverse_lazy('listar_clubes')

class ClubesDeleteView(LoginRequiredMixin, DeleteView):
    model = Clubes
    success_url = reverse_lazy('listar_clubes')

class ClubesUpdateView(LoginRequiredMixin, UpdateView):
    model = Clubes
    fields = ('nombre', 'fecha_fundacion', 'categoria_juego', 'imagen')
    success_url = reverse_lazy('listar_clubes')

class YourListView(ListView):
    model = Jugadores
    template_name = 'Basquet/panel_jugadores.html'
    context_object_name = 'jugadores'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get(search_query)
        if search_query:
            queryset = queryset.filter(attribute_icontains= search_query)
        
        return queryset

class ArticulosListView(ListView):
    model = Articulos
    template_name = 'Basquet1/panel_articulos.html'

class ArticulosDetailView(DetailView):
    model = Articulos
    success_url = reverse_lazy('articulos_inicio')

class ArticulosCreateView(LoginRequiredMixin, CreateView):
    model = Articulos
    fields = ('titulos', 'fecha_cracion', 'categoria', 'creador', 'cuerpo', 'imagen')
    success_url = reverse_lazy('articulos_inicio')

class ArticulosDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulos
    success_url = reverse_lazy('articulos_inicio')

class ArticulosUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulos
    fields = ('titulos', 'fecha_cracion', 'categoria', 'creador', 'cuerpo', 'imagen')
    success_url = reverse_lazy('articulos_inicio')    
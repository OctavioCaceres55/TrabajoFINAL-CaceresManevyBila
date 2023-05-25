from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from Basquet1.models import Entrenadores, Clubes, Jugadores, Articulos
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    fields = ('nombre', 'categoria_juego', 'fecha_fundacion','imagen')
    success_url = reverse_lazy('listar_clubes')

class ClubesDeleteView(LoginRequiredMixin, DeleteView):
    model = Clubes
    success_url = reverse_lazy('listar_clubes')

class ClubesUpdateView(LoginRequiredMixin, UpdateView):
    model = Clubes
    fields = ('nombre', 'fecha_fundacion', 'categoria_juego', 'imagen')
    success_url = reverse_lazy('listar_clubes')


# VIEWS ARTICULOS
class ArticulosListView(ListView):
    model = Articulos
    template_name= 'Basquet1/panel_articulo.html'

    

class ArticulosCreateView(CreateView):
    model = Articulos
    fields = ('titulo', 'fecha_creacion', 'categoria', 'creador', 'cuerpo', 'descriptivo')
    success_url = reverse_lazy('listar_articulo')

class ArticulosDetailView(DetailView):
    model = Articulos
    success_url = reverse_lazy('listar_articulo')

class ArticulosDeleteView(DeleteView):
    model = Articulos
    success_url = reverse_lazy('listar_articulo')

class ArticulosUpdateView(UpdateView):
    model = Articulos
    fields = ('titulo', 'fecha_creacion', 'categoria', 'creador', 'cuerpo', 'descriptivo')
    success_url = reverse_lazy('listar_articulo')
        
         

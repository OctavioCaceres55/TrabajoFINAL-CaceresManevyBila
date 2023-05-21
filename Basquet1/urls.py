"""
URL configuration for BlogBaloncesto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Basquet1.views import listar_entrenadores, listar_clubes, cargar_club, cargar_entrenador, buscar_clubes, buscar_entrenadores, eliminar_club, eliminar_entrenador, editar_entrenador, JugadoresCreateView, JugadoresDeleteView, JugadoresDetailView, JugadoresListView, JugadoresUpdateView
urlpatterns = [
    #URL ENTRENADORES
    path('entrenadores/', listar_entrenadores, name="entrenadores"),
    path('cargar-entrenador/', cargar_entrenador, name='cargar-entrenador'),
    path('buscar-entrenadores/', buscar_entrenadores, name='buscar-entrenadores'),
    path('eliminar-entrenador/<int:id>/', eliminar_entrenador, name="eliminar_entrenador"),
    path('editar-entrenador/<int:id>/', editar_entrenador, name="editar_entrenador"), 
    #URL CLUBES
    path('clubes/', listar_clubes, name="clubes"),
    path('cargar-club/', cargar_club, name="cargar-club"),
    path('buscar-clubes/', buscar_clubes, name='buscar-clubes'),
    path('eliminar-club/<int:id>/', eliminar_club, name="eliminar_club"),
    #URL JUGADORES
    path("jugadores/", JugadoresListView.as_view(), name='listar_jugadores'),
    path("jugadores/<int:pk>/", JugadoresDetailView.as_view(), name="ver_jugadores"),
    path("crear-jugadores/", JugadoresCreateView.as_view(), name="crear_jugadores"),
    path("editar-jugadres/<int:pk>/", JugadoresUpdateView.as_view(), name="editar_jugadores"),
    path("eliminar-jugadres/<int:pk>/", JugadoresDeleteView.as_view(), name="eliminar_jugadores"),
]


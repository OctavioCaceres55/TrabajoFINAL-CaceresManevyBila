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
from Basquet1.views import listar_jugadores, listar_entrenadores, listar_clubes, cargar_club, cargar_entrenador, buscar_clubes, cargar_jugador, buscar_entrenadores, buscar_jugadores

urlpatterns = [
    path('jugadores/', listar_jugadores, name="jugadores"),
    path('entrenadores/', listar_entrenadores, name="entrenadores"),
    path('clubes/', listar_clubes, name="clubes"),
    path('cargar-club/', cargar_club, name="cargar-club"),
    path('cargar-entrenador/', cargar_entrenador, name='cargar-entrenador'),
    path('buscar-clubes/', buscar_clubes, name='buscar-clubes'),
    path('cargar-jugador/', cargar_jugador, name='cargar-jugador'),
    path('buscar-entrenadores/', buscar_entrenadores, name='buscar-entrenadores'),
    path('buscar-jugadores/', buscar_jugadores, name='buscar-jugadores'),
]


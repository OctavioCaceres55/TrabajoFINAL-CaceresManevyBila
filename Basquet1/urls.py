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
from Basquet1.views import ArticulosUpdateView, ArticulosCreateView, ArticulosDeleteView, ArticulosDetailView, ArticulosListView
from Basquet1.views import EntrenadoresCreateView, EntrenadoresDeleteView, EntrenadoresDetailView, EntrenadoresListView, EntrenadoresUpdateView
from Basquet1.views import JugadoresCreateView, JugadoresDeleteView, JugadoresDetailView, JugadoresListView, JugadoresUpdateView
from Basquet1.views import ClubesCreateView, ClubesDeleteView, ClubesDetailView, ClubesListView, ClubesUpdateView
urlpatterns = [
    #URL ENTRENADORES
    path("entrenadores/", EntrenadoresListView.as_view(), name='listar_entrenadores'),
    path("entrenadores/<int:pk>/", EntrenadoresDetailView.as_view(), name="ver_entrenadores"),
    path("crear-entrenadores/", EntrenadoresCreateView.as_view(), name="crear_entrenadores"),
    path("editar-entrenadores/<int:pk>/", EntrenadoresUpdateView.as_view(), name="editar_entrenadores"),
    path("eliminar-entrenadores/<int:pk>/", EntrenadoresDeleteView.as_view(), name="eliminar_entrenadores"), 
    #URL CLUBES
    path("clubes/", ClubesListView.as_view(), name='listar_clubes'),
    path("clubes/<int:pk>/", ClubesDetailView.as_view(), name="ver_clubes"),
    path("crear-clubes/", ClubesCreateView.as_view(), name="crear_clubes"),
    path("editar-clubes/<int:pk>/", ClubesUpdateView.as_view(), name="editar_clubes"),
    path("eliminar-clubes/<int:pk>/", ClubesDeleteView.as_view(), name="eliminar_clubes"),

    #URL JUGADORES
    path("jugadores/", JugadoresListView.as_view(), name='listar_jugadores'),
    path("jugadores/<int:pk>/", JugadoresDetailView.as_view(), name="ver_jugadores"),
    path("crear-jugadores/", JugadoresCreateView.as_view(), name="crear_jugadores"),
    path("editar-jugadores/<int:pk>/", JugadoresUpdateView.as_view(), name="editar_jugadores"),
    path("eliminar-jugadres/<int:pk>/", JugadoresDeleteView.as_view(), name="eliminar_jugadores"),

    #URL ARTICULOS
    path("articulos/", ArticulosListView.as_view(), name='articulos_inicio'),
    path("articulos/<int:pk>/", ArticulosDetailView.as_view(), name="ver_articulos"),
    path("crear-articulo/", ArticulosCreateView.as_view(), name="crear_articulo"),
    path("editar-articulo/<int:pk>/", ArticulosUpdateView.as_view(), name="editar_articulo"),
    path("eliminar-articulo/<int:pk>/", ArticulosDeleteView.as_view(), name="eliminar_articulo"), 
]


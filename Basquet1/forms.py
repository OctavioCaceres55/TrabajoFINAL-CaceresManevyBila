from django import forms
from Basquet1.models import Entrenadores, Clubes, Jugadores, Aboutme, Articulo

class EntrenadoresFormulario(forms.ModelForm):
    class Meta:
        model = Entrenadores
        fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'trayectoria']
        
class JugadoresFormularios(forms.ModelForm):   
    class Meta:
        model = Jugadores
        fields = ['apellido', 'nombre', 'club','numero_camiseta','fecha_de_nacimiento', 'lugar_de_nacimiento', 'esta_habilitado']


class ClubesFormularios(forms.ModelForm):   
    class Meta:
        model = Clubes
        fields = ['nombre', 'categoria_juego', 'fecha_fundacion']

class AboutmeFormularios(forms.ModelForm):
    class Meta: 
        model = Aboutme
        fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento']


class ArticuloFormulario(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'autor', 'fecha', 'cuerpo']
    


    

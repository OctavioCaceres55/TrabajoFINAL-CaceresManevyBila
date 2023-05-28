from django import forms
from Basquet1.models import Articulos, Entrenadores, Clubes, Jugadores, Aboutme

class EntrenadoresFormulario(forms.ModelForm):
    class Meta:
        model = Entrenadores
        fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'trayectoria', 'imagen']
        
class JugadoresFormularios(forms.ModelForm):   
    class Meta:
        model = Jugadores
        fields = ['apellido', 'nombre', 'numero_camista','fecha_de_nacimiento', 'lugar_de_nacimiento', 'esta_habilitado','imagen']

class ClubesFormularios(forms.ModelForm):   
    class Meta:
        model = Clubes
        fields = ['nombre', 'categoria_juego', 'fecha_fundacion','imagen']


class ArticulosFormularios(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['titulo', 'fecha_creacion', 'categoria', 'cuerpo', 'descriptivo']

class AboutmeFormularios(forms.ModelForm):
    class Meta: 
        model = Aboutme
        fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'imagen']



    

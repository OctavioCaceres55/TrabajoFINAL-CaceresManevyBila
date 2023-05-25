from django import forms
from Basquet1.models import Articulos, Entrenadores, Clubes, Jugadores

class EntrenadoresFormulario(forms.ModelForm):
    class Meta:
        model = Entrenadores
        fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'trayectoria', 'imagen']
class JugadoresFormularios(forms.ModelForm):   
    class Meta:
        model = Jugadores
        fields = ['apellido', 'nombre', 'fecha_de_nacimiento', 'lugar_de_nacimiento', 'esta_habilitado','imagen']
class ClubesFormularios(forms.ModelForm):   
    class Meta:
        model = Clubes
        fields = ['nombre', 'categoria_juego', 'fecha_fundacion','imagen']


class ArticulosFormularios(forms.ModelForm):
    class Meta:
        model = Articulos
        fields = ['titulo', 'fecha_creacion', 'categoria', 'creador', 'cuerpo', 'descriptivo']


    

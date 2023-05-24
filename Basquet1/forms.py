from django import forms

class EntrenadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=64, required=True)
    apellido = forms.CharField(max_length=64, required=True)
    lugar_de_nacimiento = forms.CharField(max_length=256)
    fecha_de_nacimiento = forms.DateField()    
    trayectoria = forms.CharField(max_length=30000)

class JugadoresFormularios(forms.Form):   
    nombre = forms.CharField(max_length=64, required=True)
    apellido = forms.CharField(max_length=64, required=True)
    numero_camiseta = forms.IntegerField()
    lugar_de_nacimiento = forms.CharField(max_length=256, required=True)
    fecha_de_nacimiento = forms.DateField() 
    esta_habilitado = forms.BooleanField(required=True)

class ClubesFormularios(forms.Form):   
    nombre = forms.CharField(max_length=64, required=True)
    lugar_de_nacimiento = forms.CharField(max_length=256, required=True)
    fecha_fundacion = forms.DateField() 
    categoria_juego = forms.BooleanField(required=True)

class ArticulosFormularios(forms.Form):   
    titulo = forms.CharField(max_length=64, required=True)
    categoria = forms.CharField(max_length=256, required=True)
    fecha_creacion = forms.DateField() 
    cuerpo = forms.TextInput()

    

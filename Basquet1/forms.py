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
    

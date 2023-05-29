from django.db import models
from django.contrib.auth.models import User
from Basquet1.validators import validate_image_size
from datetime import date


class Jugadores(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    lugar_de_nacimiento = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()
    esta_habilitado = models.BooleanField(default=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    club = models.CharField(max_length=256, default="Agente Libre")
    numero_camiseta = models.IntegerField(default=00)


    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    lugar_de_nacimiento = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()    
    trayectoria = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Clubes(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_fundacion = models.DateField()
    categoria_juego = models.CharField(max_length=256)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return f"{self.nombre}"
    
class Aboutme(models.Model):
    nombre = models.CharField(max_length=256, null=True)
    apellido = models.CharField(max_length=256, null=True)
    lugar_de_nacimiento = models.CharField(max_length=256, null=True)
    fecha_de_nacimiento = models.DateField(null=True)    
    biografia = models.TextField(null=True)
    
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    subtitulo = models.CharField(max_length=250)
    cuerpo = models.TextField()
    fecha = models.DateField(default=date.today)
    autor = models.CharField(max_length=256, default="Anónimo")


    



    




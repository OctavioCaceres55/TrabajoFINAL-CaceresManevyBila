from django.db import models

class Jugadores(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    numero_camiseta = models.IntegerField()
    lugar_de_nacimiento = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()
    esta_habilitado = models.BooleanField(default=True)

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    lugar_de_nacimiento = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()    
    trayectoria = models.TextField()

class Clubes(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_fundacion = models.DateField()
    categoria_juego = models.CharField(max_length=256)




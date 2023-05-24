from django.db import models
from django.contrib.auth.models import User

class Jugadores(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    numero_camiseta = models.IntegerField()
    lugar_de_nacimiento = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()
    esta_habilitado = models.BooleanField(default=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    picturep = models.ImageField(upload_to='jugadores', null=True, blank=True)
    

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Entrenadores(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    lugar_de_nacimiento = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()    
    trayectoria = models.TextField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(upload_to='entrenadores', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Clubes(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_fundacion = models.DateField()
    categoria_juego = models.CharField(max_length=256)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Imagen = models.ImageField(upload_to='clubes', null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre}"

class Articulos(models.Model):
    titulo = models.CharField(max_length=256)
    fecha_creacion = models.DateField(null=True)
    categoria= models.CharField(max_length=256)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cuerpo = models.TextField()
    descriptivo = models.ImageField(upload_to='articulos', null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo}"



    




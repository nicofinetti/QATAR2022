from django.db import models

# Create your models here.
class Pais(models.Model):
    pais=models.CharField(max_length=60)

class Jugador(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    pais=models.CharField(max_length=50)
    posicion=models.CharField(max_length=25)

class Estadio(models.Model):
    localizacion=models.Charfield(max_length=30)


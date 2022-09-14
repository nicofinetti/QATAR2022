from django.db import models

# Create your models here.
class Pais(models.Model):
    pais=models.CharField(max_length=60)

class Jugador(models.Model):
    nombre=models.CharField(max_length=60)
    
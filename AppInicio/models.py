from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pais(models.Model):
    pais=models.CharField(max_length=60)

class Jugador (models.Model):
    nombre=models.CharField(max_length=50,blank=True, null=True)
    apellido=models.CharField(max_length=50,blank=True, null=True)
    edad=models.IntegerField(blank=True, null=True)
    pais=models.CharField(max_length=50,blank=True, null=True)
    equipo=models.CharField(max_length=50,blank=True, null=True)
    posicion=models.CharField(max_length=50,blank=True, null=True)

    def __str__ (self):
        return f"{self.nombre} {self.apellido} - {self.pais}"

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares', null=True, blank=True)
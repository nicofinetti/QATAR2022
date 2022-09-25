from django.db import models
class Pais(models.Model):
    grupo=models.CharField(max_length=1)
    instanciaplayoff=models.CharField(max_length=25)
    jugadores=models.CharField(max_length=25)
class Jugador(models.Model):
    nombre=models.CharField(max_length=60)
    equipo=models.CharField(max_length=50)
    posicion=models.CharField(max_length=25)

class Estadio(models.Model):
    localizacion=models.CharField(max_length=30)

class FechaGrupos(models.Model):
    equipolocal=models.CharField(max_length=25)
    equipovisita=models.CharField(max_length=25)
    fecha=models.CharField(max_length=25)
    resultado=models.CharField(max_length=25)

class FechaPlayOff(models.Model):
    equipolocal=models.CharField(max_length=25)
    equipovisita=models.CharField(max_length=25)
    fecha=models.DateField()
    resultado=models.CharField(max_length=25)


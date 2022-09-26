from django.db import models
class Pais(models.Model):
    grupo=models.CharField('Nombre del grupo', max_length=1)
    instanciaplayoff=models.CharField(max_length=25)
    jugadores=models.CharField(max_length=25)

    def __str__(self):
        return self.grupo
class Jugador(models.Model):
    nombre=models.CharField('Nombre completo del jugador', max_length=60)
    equipo=models.ForeignKey(Pais, blank=True, null=True, on_delete=models.CASCADE)
    posicion=models.CharField('Posicion en la que juega', max_length=25)
    sancionado=models.BooleanField(null=False)
    lesionado=models.BooleanField(null=False)

    def __str__(self):
        return self.nombre
class Estadio(models.Model):
    ubicacion=models.CharField('Direccion del estadio', max_length=30)
    nombre=models.CharField('Nombre oficial del estadio', max_length=30)

    def __str__(self):
        return self.nombre

class FechaGrupos(models.Model):
    equipolocal=models.CharField(max_length=25)
    equipovisita=models.CharField(max_length=25)
    fecha=models.DateTimeField()
    resultado=models.CharField(max_length=25)
    estadio=models.CharField('Nombre oficial del estadio', max_length=30)

    def __str__(self):
        return self.fecha
class FechaPlayOff(models.Model):
    equipolocal=models.CharField(max_length=25)
    equipovisita=models.CharField(max_length=25)
    fecha=models.DateField()
    resultado=models.CharField(max_length=25)
    estadio=models.CharField('Nombre oficial del estadio', max_length=30, null=True)

    def __str__(self):
        return self.fecha

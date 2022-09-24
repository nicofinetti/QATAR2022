from django.db import models
from datetime import datetime

# Create your models here.
class Sala(models.Model):
    nombre = models.CharField(max_length=1000)
    
class Mensaje(models.Model):
    valor = models.CharField(max_length=1000000)
    fecha = models.DateTimeField(default=datetime.now, blank=True)
    usuario = models.CharField(max_length=1000000)
    sala = models.CharField(max_length=1000000)
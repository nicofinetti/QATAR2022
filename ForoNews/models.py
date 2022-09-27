from django.db import models

class Foro(models.Model):
    usuario=models.CharField(max_length=200,default="anonimo")  #incorporar model de usuario registrado
    email=models.CharField(max_length=200,null=True)            #incorporar mismo model de arriba
    tema= models.CharField(max_length=300)
    descripcion = models.CharField(max_length=1000,blank=True)
    enlace = models.CharField(max_length=100 ,null =True)
    fecha_creado=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.tema)

class Discusion(models.Model):
    foro = models.ForeignKey(Foro, blank=True, on_delete=models.CASCADE)
    discutir = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.foro)


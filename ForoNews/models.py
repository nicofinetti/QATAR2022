from django.db import models
from django.contrib.auth.models import User
#from django.utils.text import slugify


STATUS = (
    (0,"Borrador"),
    (1,"Publicado")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog')
    fecha_actualizado = models.DateTimeField(auto_now= True)
    content = models.TextField()
    fecha_creado = models.DateTimeField(auto_now_add=True)
    estatus = models.IntegerField(choices=STATUS, default=0)
    imagen = models.ImageField(upload_to='pics', null = True, blank = True)


    class Meta:
        ordering = ['-fecha_creado']

    #test de slugify para no tener que poner el slug manualmente 

    #def save(self, *args, **kwargs):
        #self.slug = slugify(self.titulo)
        #super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo


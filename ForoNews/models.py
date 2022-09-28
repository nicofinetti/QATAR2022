from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()  #implementar con usuario y avatar ya creados
		
    def __str__(self):
        return self.user.usuario

class Categoria(models.Model):
    titulo = models.CharField(max_length=20)
    subtitulo = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    resumen = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categorias = models.ManyToManyField(Categoria)
    featured = models.BooleanField()
    imagen = models.ImageField()

    def __str__(self):
        return self.title

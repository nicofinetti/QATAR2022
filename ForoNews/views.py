from django.views import generic
from .models import Post

class ListaPosts(generic.ListView):
    queryset = Post.objects.filter(estatus=1).order_by('-fecha_creado')
    template_name = '../templates/AppInicio/inicio.html'

class DetallePost(generic.DetailView):
    model = Post
    template_name = '../templates/AppInicio/detalle_post.html'


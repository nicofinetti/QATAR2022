from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404


class ListaPosts(generic.ListView):
    queryset = Post.objects.filter(estatus=1).order_by('-fecha_creado')
    nombre_plantilla = '../templates/AppInicio/inicio.html'

class DetallePost(generic.DetailView):
    model = Post
    nombre_plantilla = '../templates/AppInicio/detalle_post.html'

def Post_Detallado(request, slug):
    nombre_plantilla = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comentarios = post.comentarios.filter(active=True)
    nuevo_comentario = None
    # comentario subido
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # para crear comentario sin subir a la db aun
            nuevo_comentario = comment_form.save(commit=False)
            # reasignar comentario al post
            nuevo_comentario.post = post
            # guardar comentario en la db
            nuevo_comentario.save()
    else:
        comment_form = CommentForm()

    return render(request, nombre_plantilla, {'post': post,
                                           'comentarios': comentarios,
                                           'nuevo_comentario': nuevo_comentario,
                                           'comment_form': comment_form})

#FALTA TRADUCIR AL ESPAÑOL ALGUNAS VARIABLES, Y MODIFICAR LAS COSAS PARA QUE FUNCIONE! 
from django.shortcuts import render
from django.db.models import Q
from .models import Post, Categoria, Autor

def inicio(request):
    categorias = Categoria.objects.all()[0:3]
    destacado = Post.objects.filter(featured=True)
    reciente = Post.objects.order_by('-fecha_creacion')[0:3]
    context= {
        'lista_objetos': destacado,
        'reciente': reciente,
        'categorias': categorias,
    }
    return render(request, 'inicio.html', context)

def post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)

def acerca_de (request):
    return render(request, 'about_page.html')  #about debe redirigir a nuestra pagina de info personal

def lista_post_categorias (request, slug):
    categoria = Categoria.objects.get(slug = slug)
    posts = Post.objects.filter(categories__in=[categoria])
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)    

def todoslosposts(request):
    posts = Post.objects.order_by('-fecha_creacion')
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)  #faltaria crear la pagina "todos los posts"

def busqueda(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'search_bar.html', context)  #redirigir a busqueda ya creada


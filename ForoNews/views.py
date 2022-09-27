from django.shortcuts import render, redirect
from .models import * 
from .forms import * 
 
def forogeneral(request):
    foros = Foro.objects.all()
    cantidad_posts = foros.count()
    discusiones = []
    for elemento in foros:
        discusiones.append(elemento.discusiones_set.all())
 
    contexto = {'foros' : foros,
                'cantidad_posts' : cantidad_posts,
                'discusiones' : discusiones}
    return render(request, '../templates/ForoNews/forogeneral.html', contexto)
 
def agregarenforo(request): 
    form = CrearEnForo()
    if request.method == 'POST':
        form = CrearEnForo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto ={'form' : form}
    return render(request, '../templates/ForoNews/agregarenforo.html', contexto)
 
def agregarendiscusion(request):
    form = agregarendiscusion()
    if request.method == 'POST':
        form = agregarendiscusion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto ={'form' : form}
    return render(request, '../templates/ForoNews/agregarendiscusion.html', contexto)

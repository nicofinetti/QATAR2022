from django.conf import settings
from django.urls import path
from django.contrib import admin
from ForoNews.views import inicio, post, acerca_de, busqueda, lista_post_categorias, todoslosposts  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name = 'inicio'),
    path('post/<slug>/', post, name = 'post'),
    path('acerca_de/', acerca_de,name = 'acerca_de' ),
    path('lista_post_categorias/<slug>/', lista_post_categorias, name = 'lista_post_categorias'),
    path('posts/', todoslosposts, name = 'todoslosposts'),
    path('busqueda/', busqueda, name = 'busqueda'),

]

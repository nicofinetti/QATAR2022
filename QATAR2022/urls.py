from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppFutbol.urls')),
    path('', include('ForoNews.urls')),
    path('', include('GestionUsuario.urls')),
    path('', include('Mensajeria.urls')),
]

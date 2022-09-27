from django.urls import path
from AppInicio import views
from .views import *

urlpatterns= [

    path('',views.inicio, name='inicio'),
    path('calendario/',views.calendario, name= 'calendario'),
    path('comenta/',views.comenta, name= 'comenta'),
    path('comparte/',views.comparte, name= 'comparte'),
    path('estadios/',views.estadios, name= 'estadios'),
    path('grupos/',views.grupos, name= 'grupos'),
    path('invita/',views.invita, name= 'invita'),
    path('miequipo/',views.miequipo, name= 'miequipo'),
    path('mimundial/',views.mimundial, name= 'mimundial'),
    path('mispredicciones/',views.mispredicciones, name= 'mispredicciones'),
    path('paises/',views.paises, name= 'paises'),
    path('resultados/',views.resultados, name= 'resultados'),
    path('sobrenos/',views.sobrenos, name= 'sobrenos'),
    path('iniciaSesion/',views.iniciaSesion, name= 'iniciaSesion'),
    
           
]

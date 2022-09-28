from django.urls import path
from AppInicio import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns= [

    path('',views.inicio, name='inicio'),
    path('calendario/',views.calendario, name= 'calendario'),
    path('comenta/',views.comenta, name= 'comenta'),
    path('comparte/',views.comparte, name= 'comparte'),
    path('estadios/',views.estadios, name= 'estadios'),
    path('grupos/',views.grupos, name= 'grupos'),
    path('mensajes/',views.mensajes, name= 'mensajes'),
    path('miequipo/',views.miequipo, name= 'miequipo'),
    path('mimundial/',views.mimundial, name= 'mimundial'),
    path('mispredicciones/',views.mispredicciones, name= 'mispredicciones'),
    path('paises/',views.paises, name= 'paises'),
     path('jugadores/',views.jugadores, name= 'jugadores'),
    path('resultados/',views.resultados, name= 'resultados'),
    path('sobrenos/',views.sobrenos, name= 'sobrenos'),
    path('jugadorFormulario/', views.jugadorFormulario, name='jugadorFormulario'),

    path('login',views.login_request,name='login'),
    path('register',views.register, name='Register'),
    path('logout',LogoutView.as_view(template_name="AppInicio/logout.html"),name='Logout'),
    path('editarPerfil',views.editarPerfil, name="EditarPerfil"),
    

           
]

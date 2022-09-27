from django.contrib import admin
from django.urls import path
from ForoNews.forms import CrearEnDiscusion
from . import views
from .views import *


urlpatterns = [
    #path('admin/', admin.site.urls),               Esto no va aca
    path('forogeneral/', views.forogeneral, name="forogeneral"),
    path('agregarenforo/', views.agregarenforo, name='agregarenforo'),
    path('agregarendiscusion/', views.agregarendiscusion, name='agregarendiscusion'),
]
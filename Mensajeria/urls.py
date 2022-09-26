from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/', views.mensajes, name="mensajes"),

]
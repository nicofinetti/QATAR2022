from django.urls import path
from AppInicio import views
from .views import *

urlpatterns= [

    path('',views.inicio, name='inicio'),
           
]

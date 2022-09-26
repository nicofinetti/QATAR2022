from django.urls import path
from . import views

urlpatterns = [
    path('forogeneral/', views.forogeneral, name="forogeneral"),

]
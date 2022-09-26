from django.shortcuts import render
import os

def inicio(request):
    return render(request, '../templates/AppFutbol/inicio.html', {})